from prefect import Flow, task, case, apply_map
from prefect.tasks.control_flow import merge

@task
def inc(x):
    return x + 1

@task
def negate(x):
    return -x

@task
def is_even(x):
    return x % 2 == 0

def inc_or_negate(x):
    cond = is_even(x)
    # If x is even, increment it
    with case(cond, True):
        res1 = inc(x)
    # If x is odd, negate it
    with case(cond, False):
        res2 = negate(x)
    return merge(res1, res2)

with Flow("apply-map example") as flow:
    result = apply_map(inc_or_negate, range(4))

flow.run()
