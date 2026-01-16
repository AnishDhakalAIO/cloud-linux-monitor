from src.utils.logger import get_logger
from src.core.cpu import get_cpu_usage
from src.core.memory import get_memory_usage
from src.core.disk import get_disk_usage
from src.core.network import get_network_usage
import time
from datetime import datetime

logger = get_logger()

def run_monitor():

    print("\n===== cloud Linux monitor =====\n")

    try:
        while True:
            logger.info("===== Monitoring Cycle Start =====")
            logger.info(f"Timestamp: {datetime.now()}")

            get_cpu_usage()
            get_memory_usage()
            get_disk_usage()
            get_network_usage()

            time.sleep(5)

    except KeyboardInterrupt:
        print("\nmonitoring stopped by user.")
        logger.info("===== Monitoring stopped manually =====")


if __name__ == "__main__":
    run_monitor()