import os
from prefect import task, Flow
from prefect.engine.results import LocalResult


def format_location(date, task_name, **kwargs):
    return os.path.join(
        os.path.expanduser("~"), f"{date.year}-{date.month}_{task_name}.prefect"
    )

@task(result=LocalResult(location=format_location))
def my_task():
    return [1, 2, 3, 4]

with Flow("local-result-with-date-parsing") as flow:
    my_task()

flow.run()