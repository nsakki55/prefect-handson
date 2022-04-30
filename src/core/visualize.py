from prefect import task, Flow, Parameter
from prefect.tasks.control_flow import switch

@task
def handle_zero():
    return float('nan')

with Flow("math") as flow:
    x, y = Parameter("x"), Parameter("y")
    a = x + y
    switch(a, cases={0: handle_zero(), 1: 6 / a})

flow.visualize()