from prefect import Flow, task, flatten

@task
def A():
    return [1, 2, 3]

@task
def B(x):
    return list(range(x))

@task
def C(y):
    return y + 100

with Flow('flat map') as f:
    a = A() # [1, 2, 3]
    b = B.map(x=a) # [[0], [0, 1], [0, 1, 2]]
    c = C.map(y=flatten(b)) # [100, 100, 101, 100, 101, 102]
f.run()