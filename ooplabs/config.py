# ooplabs/config.py

"""
Configuration module for the OOP Labs project.

This file defines global constants and setup routines that other modules import.
It controls things like logging levels, file paths, and environment variables.
"""

import os                   # Import to access environment variables
from pathlib import Path    # Import to manage file paths in a cross-platform way

# ---------------------------------------------------------------------------
# Define the base directory of the project dynamically
# ---------------------------------------------------------------------------
BASE_DIR: Path = Path(__file__).resolve().parent  # Resolved directory of this config file

# ---------------------------------------------------------------------------
# Define a logs directory and ensure it exists
# ---------------------------------------------------------------------------
LOGS_DIR: Path = BASE_DIR / "logs"  # Logs folder inside ooplabs/
LOGS_DIR.mkdir(exist_ok=True)       # Create if not present

# ---------------------------------------------------------------------------
# Retrieve the logging level from an environment variable, default to INFO
# ---------------------------------------------------------------------------
LOG_LEVEL: str = os.getenv("OOPLAB_LOG_LEVEL", "INFO").upper()  # Default to INFO if not set

# ---------------------------------------------------------------------------
# Define default log file path
# ---------------------------------------------------------------------------
LOG_FILE: Path = LOGS_DIR / "app.log"  # Single log file for entire project

# ---------------------------------------------------------------------------
# Other potential configuration entries (extendable)
# ---------------------------------------------------------------------------
PROJECT_NAME: str = "OOP Labs Vehicle Simulation System"
VERSION: str = "1.0.0"