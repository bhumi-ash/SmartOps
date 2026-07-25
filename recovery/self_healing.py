from recovery.recovery_engine import restart_container


def auto_heal(containers):

    recovery_results = []

    for container in containers:

        if container["status"] == "exited":

            result = restart_container(container["name"])

            recovery_results.append(result)

    return recovery_results