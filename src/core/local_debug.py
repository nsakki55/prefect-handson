import prefect
from prefect import task, Flow
from prefect.engine.flow_runner import FlowRunner
from prefect.executors import LocalExecutor

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow("hello-flow") as flow:
    hello_task()

# runner = FlowRunner(flow=flow)
# flow_state = runner.run(return_tasks=flow.tasks)

state = flow.run(executor=LocalExecutor())