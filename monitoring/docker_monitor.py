import docker


def get_container_metrics():

    client = docker.from_env()

    running = client.containers.list()

    all_containers = client.containers.list(all=True)

    container_details = []

    exited = 0

    for container in all_containers:

        if container.status == "exited":
            exited += 1

        container_details.append({

            "name": container.name,

            "status": container.status

        })

    return {

        "running_containers": len(running),

        "exited_containers": exited,

        "total_containers": len(all_containers),

        "containers": container_details

    }