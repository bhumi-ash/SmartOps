import docker


def get_container_metrics():
    client = docker.from_env()

    running = client.containers.list()

    all_containers = client.containers.list(all=True)

    container_details = []

    for container in all_containers:

        container_details.append({

            "name": container.name,

            "status": container.status

        })

    return {

        "running_containers": len(running),

        "containers": container_details

    }