import psutil
from src.utils.logger import get_logger
from src.config.settings import DISK_THRESHOLD
logger = get_logger()



def get_disk_usage ():
    usage = psutil.disk_usage("/").percent
    logger.info(f"Disk Usage : {usage}%")

    if usage >= DISK_THRESHOLD:
        print(f"ALERT! Disk usage has reched {usage}%")
    print(f"Disk usage : {usage}%")
    return usage

if __name__ == "__main__":
    get_disk_usage()