import prefect
from prefect import task, Flow

@task
def add_one(x):
    """Operates one number at a time"""
    return x + 1

@task(name="sum")
def sum_numbers(y):
    """Operates on an iterable of numbers"""
    result = sum(y)
    logger = prefect.context["logger"]
    logger.info("The sum is {}".format(result))
    return result


## Imperative API
flow = Flow("Map Reduce")
flow.set_dependencies(add_one, keyword_tasks={"x": [1, 2, 3, 4]}, mapped=True)
flow.set_dependencies(sum_numbers, keyword_tasks={"y": add_one})
# flow.run()
flow.visualize()

# ## Functional API
# with Flow("Map Reduce") as flow:
#     mapped_result = add_one.map(x=[1, 2, 3, 4])
#     summed_result = sum_numbers(mapped_result)