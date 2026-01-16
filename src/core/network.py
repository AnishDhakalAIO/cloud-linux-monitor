import psutil
from src.utils.logger import get_logger

logger = get_logger()

def get_network_usage():

    net_io = psutil.net_io_counters()

    sent = net_io.bytes_sent
    received = net_io.bytes_recv

    logger.info(f"Network usage - sent : {sent} bytes, Received: {received} bytes")

    print(f"Network usage - sent : {sent} bytes, Received: {received} bytes")

    return sent, received



if __name__ == "__main__":
    get_network_usage()