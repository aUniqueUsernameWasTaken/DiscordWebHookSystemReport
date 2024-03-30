import psutil

def getUsage():
    important_factors = [
        "CPU usage  | " + str(psutil.cpu_percent()) + "%",
        "Ram usage  | " + str(psutil.virtual_memory().percent) + "%",
        "Swap usage | " + str(psutil.swap_memory().percent) + "%",
        "Disk usage | " + str(psutil.disk_usage('/').percent) + "%",
    ]
    return important_factors

