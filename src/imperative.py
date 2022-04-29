from prefect import Task, Flow

class RunMeFirst(Task):
    def run(self):
        print("I'm running first!")

class PlusOneTask(Task):
    def run(self, x):
        return x + 1

flow = Flow('My Imperative Flow')
plus_one = PlusOneTask()
flow.set_dependencies(
    task=plus_one,
    upstream_tasks=[RunMeFirst()],
    keyword_tasks=dict(x=10))

flow.visualize()