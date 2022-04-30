from typing import Tuple
from prefect import Flow, task

@task(nout=2)
def inc_and_dec(x):
    return x + 1, x -1

@task
def double_and_triple(x: int) -> Tuple[int, int]:
    return x * 2, x * 3

def main():
    with Flow("Using Multi Values") as flow:
        inc, dec = inc_and_dec(1)
        double, triple = double_and_triple(inc)

    flow.run()

if __name__ == "__main__":
    main()
