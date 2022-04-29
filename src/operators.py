import random
from prefect import Flow, task

@task
def a_number():
    return random.randint(0, 100)

def main():
    with Flow("Using Operators") as flow:
        a = a_number()
        b = a_number()

        add = a + b
        sub = a - b
        lt = a < b

    flow.run()

if __name__ == "__main__":
    main()
