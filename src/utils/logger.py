import logging
import os

def trim_log_file(log_file, max_lines=5):
    """Keep only the last `max_lines` entries in the log file."""
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            lines = f.readlines()
        if len(lines) > max_lines:
            lines = lines[-max_lines:]  # keep last max_lines
            with open(log_file, "w") as f:
                f.writelines(lines)

def get_logger():
    """Logger that keeps last 5 entries."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "monitor.log")

    # Trim old entries first
    trim_log_file(log_file, max_lines=5)

    logger = logging.getLogger("cloud-monitor")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    # Append mode so new logs are added
    file_handler = logging.FileHandler(log_file, mode="a")

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
