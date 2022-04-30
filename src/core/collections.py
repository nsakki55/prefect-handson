import random
from prefect import Flow, task

@task
def a_number():
    return random.randint(0, 100)

@task
def get_sum(x):
    print(x)
    return x

def main():
    with Flow("Using Operators") as flow:
        a = a_number()
        b = a_number()
        s = get_sum([a, b])

    flow.run()

if __name__ == "__main__":
    main()
