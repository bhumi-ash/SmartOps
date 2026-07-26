from recovery.recovery_engine import restart_container
from incidents.incident_manager import log_incident


def auto_heal(containers):

    recovery_results = []

    for container in containers:

        if container["status"] == "exited":

            result = restart_container(container["name"])

            log_incident(result)

            recovery_results.append(result)

    return recovery_results