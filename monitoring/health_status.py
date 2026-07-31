def get_health_status(system_metrics, container_metrics, recoveries):

    cpu = system_metrics["cpu"]
    ram = system_metrics["ram"]
    disk = system_metrics["disk"]

    running = container_metrics.get("running_containers", 0)
    exited = container_metrics.get("exited_containers", 0)

    if exited > 0:

        return {
            "status": "Critical",
            "color": "#ef4444",
            "message": "One or more Docker containers are stopped."
        }

    if cpu > 80:

        return {
            "status": "Warning",
            "color": "#facc15",
            "message": "CPU usage is above 80%."
        }

    if ram > 80:

        return {
            "status": "Warning",
            "color": "#facc15",
            "message": "RAM usage is above 80%."
        }

    if disk > 90:

        return {
            "status": "Warning",
            "color": "#facc15",
            "message": "Disk usage is above 90%."
        }

    return {
        "status": "Healthy",
        "color": "#22c55e",
        "message": "Everything is operating normally."
    }