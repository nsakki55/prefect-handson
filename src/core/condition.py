from random import random

from prefect import task, Flow, case
from prefect.tasks.control_flow import merge


@task
def check_condition():
    return random() < 0.5


@task
def action_if_true():
    return "I am true!"


@task
def action_if_false():
    return "I am false!"


@task(log_stdout=True)
def another_action(val):
    print(val)


with Flow("Example: Conditional Tasks") as flow:
    cond = check_condition()

    with case(cond, True):
        val_if_true = action_if_true()

    with case(cond, False):
        val_if_false = action_if_false()

    val = merge(val_if_true, val_if_false)

    another_action(val)


if __name__ == "__main__":
    flow.run()
    flow.visualize()