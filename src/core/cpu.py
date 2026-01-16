import psutil
from src.utils.logger import get_logger

logger = get_logger()

cpu_threshold = 50.0 

def get_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    logger.info(f"CPU usage: {usage}%")

    if usage >= cpu_threshold:
        print("cpu is over used ALERT !")

    print(f"CPU usage: {usage}%")
    return usage



if __name__ == "__main__":
    get_cpu_usage()
