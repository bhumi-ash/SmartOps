from flask import render_template

from app import app

from monitoring.system_monitor import get_system_metrics

from monitoring.docker_monitor import get_container_metrics

from recovery.self_healing import auto_heal


@app.route("/")
def dashboard():

    metrics = get_system_metrics()
    container_data = get_container_metrics()
    recovery_results = auto_heal(container_data["containers"])

    return render_template(
        "dashboard.html",
        cpu=metrics["cpu"],
        ram=metrics["ram"],
        disk=metrics["disk"],
        containers=container_data["running_containers"]
    )