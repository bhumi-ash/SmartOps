from flask import render_template

from app import app

from monitoring.system_monitor import get_system_metrics


@app.route("/")
def dashboard():

    metrics = get_system_metrics()

    return render_template(

        "dashboard.html",

        cpu=metrics["cpu"],

        ram=metrics["ram"],

        disk=metrics["disk"]

    )