import random
from prefect import Flow, task, unmapped

@task
def add(x, y):
    return x + y

def main():
    with Flow("Using Mapping") as flow:
        add.map(x=[1, 2, 3], y=unmapped(1))


    flow.run()

if __name__ == "__main__":
    main()
