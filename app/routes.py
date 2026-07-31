from flask import render_template

from app import app

from monitoring.system_monitor import get_system_metrics

from monitoring.docker_monitor import get_container_metrics

from recovery.self_healing import auto_heal

from incidents.incident_manager import get_incidents

from recovery.recovery_activity import get_recoveries

from monitoring.health_status import get_health_status


@app.route("/")
def dashboard():

    metrics = get_system_metrics()
    container_data = get_container_metrics()
    recovery_results = auto_heal(container_data["containers"])
    incidents = get_incidents()
    recoveries = get_recoveries()
    health = get_health_status(
    system_metrics,
    container_data,
    recoveries
)

    return render_template(
        "dashboard.html",
        cpu=metrics["cpu"],
        ram=metrics["ram"],
        disk=metrics["disk"],
        containers=container_data["running_containers"],
        incidents=incidents,
        recoveries=recoveries,
        health=health
    )