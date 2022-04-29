from prefect import Flow, task


@task
def add(x, y):
    return x + y


def main():
    with Flow("Flow With Constants") as flow:
        add(1, 2)

    assert len(flow.tasks) == 1
    assert len(flow.constants) == 2

    flow.run()


if __name__ == "__main__":
    main()
