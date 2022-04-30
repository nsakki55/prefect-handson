from prefect import Flow, task

numbers = [1, 2, 3]
map_fn = task(lambda x: x + 1)
reduce_fn = task(lambda x: sum(x))

with Flow('Map Reduce') as flow:
    mapped_result = map_fn.map(numbers)
    reduced_result = reduce_fn(mapped_result)

state = flow.run()
assert state.result[reduced_result].result == 9
