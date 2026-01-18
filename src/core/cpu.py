import psutil
from src.utils.logger import get_logger
from src.config.settings import CPU_THRESHOLD

logger = get_logger()



def get_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    logger.info(f"CPU usage: {usage}%")

    if usage >= CPU_THRESHOLD:
        print("cpu is over used ALERT !")

    print(f"CPU usage: {usage}%")
    return usage



if __name__ == "__main__": 
    get_cpu_usage()
