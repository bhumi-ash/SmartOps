from recovery.recovery_engine import restart_container
from incidents.incident_manager import log_incident
from notifications.email_notifier import send_email
from recovery.recovery_activity import log_recovery


def auto_heal(containers):

    recovery_results = []

    for container in containers:

        if container["status"] == "exited":

            result = restart_container(container["name"])

            log_incident(result)

            log_recovery(result)

            send_email(result)

            recovery_results.append(result)

    return recovery_results