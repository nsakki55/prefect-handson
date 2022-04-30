from prefect import task, Flow

@task(task_run_name="{val}")
def compute(val):
    pass

with Flow("template-example") as flow:
    compute(val="hello")

flow.run()