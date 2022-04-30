# flow.py
from prefect.engine.results import LocalResult, PrefectResult
from prefect import task, Flow, Task

@task(result=PrefectResult())
def add(x, y=1):
    return x + y

class AddTask(Task):
    def run(self, x, y):
        return x + y

a = AddTask(result=LocalResult(dir="~/.prefect/results"))

# send the configuration to the Flow object
with Flow("my handled flow!", result=LocalResult()) as flow:
    first_result = add(1, y=2)
    second_result = add(x=first_result, y=100)

flow.run()