from prefect.tasks.secrets import PrefectSecret
from prefect import task, Flow
from prefect.tasks.secrets import EnvVarSecret

p = PrefectSecret("foo")
print(p.run())

@task
def print_value(x):
    print(x)

with Flow("Example") as flow:
    secret = EnvVarSecret("FOO")
    print_value(secret)
flow.run()