import prefect
from prefect import Flow, task

@task(log_stdout=True)
def my_task():
    logger = prefect.context.get("logger")

    logger.info("An info message.")
    logger.warning("A warning message.")


with Flow("Logging") as flow:
    my_task()
flow.run()


