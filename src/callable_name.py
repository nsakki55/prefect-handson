from prefect import task, Flow


def generate_task_run_name(val: str, **kwargs):
    """
    Replace spaces with '-' and truncate at 10 characters.

    You can specify some arguments if you know they will be passed, but you must take
    **kwargs to consume the rest of the passed values from the context or an exception
    will be thrown.
    """
    val = val.replace(" ", "-")
    if len(val) > 10:
        val = val[:10]
    return val

@task(task_run_name=generate_task_run_name)
def compute(val: str):
    pass

with Flow("template-example") as flow:
    compute(val="hello this is a kind of long sentence")

state = flow.run()
print(state._result.value)