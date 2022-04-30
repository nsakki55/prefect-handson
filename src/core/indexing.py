import random
from prefect import Flow, task

@task
def fn():
    return {"a": 1, "b": 2}

def main():
    with Flow("Using Indexing") as flow:
        x = fn()
        y = x["a"]

    flow.run()

if __name__ == "__main__":
    main()
