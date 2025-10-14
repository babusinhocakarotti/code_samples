# ooplabs/utils/logging.py

"""
Logging configuration module.
This module provides a factory function to get project-wide configured loggers.
The log level is dynamically controlled using environment variables.
"""

import logging                                      # Core Python logging library
from logging.handlers import RotatingFileHandler    # For auto-rotating logs
from ooplabs.config import LOG_FILE, LOG_LEVEL      # Import centralized configuration

# ---------------------------------------------------------------------------
# Function to configure and get a logger
# ---------------------------------------------------------------------------
def get_logger(name: str) -> logging.Logger:
    """
    Returns a pre-configured logger instance with console and file handlers.

    Args:
        name (str): Name of the logger (usually __name__)

    Returns:
        logging.Logger: Configured logger ready for use
    """

    # Create a new logger instance with given name
    logger = logging.getLogger(name)

    # If already configured, don’t duplicate handlers
    if logger.handlers:
        return logger

    # Set the logging level according to environment or config
    logger.setLevel(LOG_LEVEL)

    # --- 1. Create formatter ---
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # --- 2. Create console handler ---
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # --- 3. Create file handler (rotating log file) ---
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=2 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # --- 4. Optional: suppress overly verbose logs from other modules ---
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Log startup confirmation for debugging
    logger.info(f"Logger started with level={LOG_LEVEL}, output={LOG_FILE}")

    return logger