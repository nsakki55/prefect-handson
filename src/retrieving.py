from prefect import Flow, task

@task(name="task1")
def func(x):
    return x**2


@task(name="task2")
def func2(x):
    return x**2

@task(name="task3")
def func3(x):
    return x**2


def main():
    with Flow("Retrieving") as flow:
        a = func(1)
        b = func(2)
        c = func(3)
        flow.get_tasks(name="task1")
    flow.run()
if __name__ == "__main__":
    main()
