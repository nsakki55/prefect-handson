from random import randrange

from prefect import task, Flow, Parameter
from prefect.executors import LocalDaskExecutor

@task
def random_num(stop):
    number = randrange(stop)
    print(f"Your number is {number}")
    return number

@task
def sum_numbers(numbers):
    print(sum(numbers))

with Flow("parallel-execution") as flow:
    stop = Parameter("stop")

    number_1 = random_num(stop)
    number_2 = random_num(stop)
    number_3 = random_num(stop)

    sum_numbers = sum_numbers(numbers=[number_1, number_2, number_3])

flow.run(parameters={"stop": 5}, executor=LocalDaskExecutor())

