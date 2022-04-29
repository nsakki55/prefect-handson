from prefect import task, Flow
from prefect.engine import signals


def alert_on_special_failure(task, old_state, new_state):
    if new_state.is_failed():
        if getattr(new_state.result, "flag", False) is True:
            print("Special failure mode!  Send all the alerts!")
            print("a == b == {}".format(new_state.result.value))

    return new_state


@task(state_handlers=[alert_on_special_failure])
def mission_critical_task(a, b):
    if a == b:
        fail_signal = signals.FAIL("a equaled b!")
        fail_signal.flag = True
        fail_signal.value = a
        raise fail_signal
    else:
        return 1 / (b - a)


with Flow(name="state-inspection-handler") as flow:
    result = mission_critical_task(1, 1)

flow.run()
# Special failure mode!  Send all the alerts!
# a == b == 1
