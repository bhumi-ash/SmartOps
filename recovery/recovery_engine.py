import docker


def restart_container(container_name):
    client = docker.from_env()

    try:
        container = client.containers.get(container_name)

        container.restart()

        return {
            "success": True,
            "container": container_name,
            "action": "restart",
            "message": "Container restarted successfully"
        }

    except docker.errors.NotFound:
        return {
            "success": False,
            "container": container_name,
            "action": "restart",
            "message": "Container not found"
        }

    except Exception as e:
        return {
            "success": False,
            "container": container_name,
            "action": "restart",
            "message": str(e)
        }