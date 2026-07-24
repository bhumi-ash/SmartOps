import psutil


def get_system_metrics():

    cpu = psutil.cpu_percent(interval=1) #CPU usage last second.

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    return {

        "cpu": cpu,

        "ram": ram,        #returning a dictionary

        "disk": disk

    }