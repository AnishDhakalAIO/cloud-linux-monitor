import psutil
from src.utils.logger import get_logger

logger = get_logger()

disk_threashold = 60.0

def get_disk_usage ():
    usage = psutil.disk_usage("/").percent
    logger.info(f"Disk Usage : {usage}%")

    if usage >= disk_threashold:
        print(f"ALERT! Disk usage has reched {usage}%")
    print(f"Disk usage : {usage}%")
    return usage

if __name__ == "__main__":
    get_disk_usage()