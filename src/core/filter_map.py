from prefect import task, Flow, context
from prefect.tasks.control_flow.filter import FilterTask
from prefect.engine.signals import SKIP

filter_results = FilterTask(
    filter_func=lambda x: not isinstance(x, (BaseException, SKIP, type(None)))
)


@task
def unstable_task(arg):
    if arg == 1:
        raise RuntimeError("Fail this task execution")
    if arg == 2:
        raise SKIP("Skip this task execution")
    if arg == 3:
        return None

    return arg


@task
def add_one(arg):
    return arg + 1


@task
def log_args(args):
    logger = context.get("logger")
    logger.info(args)


with Flow('filter') as flow:
    raw_out = unstable_task.map([0, 1, 2, 3, 4])
    # raw_out is [0, RuntimeError, SKIP, None, 4] at this point

    filtered = filter_results(raw_out)
    inc_out = add_one.map(filtered)

    log_args(inc_out)
    # [1, 5]

flow.run()