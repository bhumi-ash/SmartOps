import docker


def get_container_metrics():
    client = docker.from_env()

    containers = client.containers.list()

    return {
        "running_containers": len(containers)
    }