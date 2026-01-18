from src.utils.logger import get_logger
import psutil
from src.config.settings import MEMORY_THRESHOLD
logger = get_logger()



def get_memory_usage():
    """Fetch Memory usage percentage, log it, and return."""
    usage = psutil.virtual_memory().percent
    logger.info(f"Memory usage: {usage}%")

    if usage >= MEMORY_THRESHOLD:
        print(f"ALERT! Memory usage is high: {usage}%")

    print(f"Memory usage: {usage}%")
    return usage

if __name__ == "__main__":
    get_memory_usage()
