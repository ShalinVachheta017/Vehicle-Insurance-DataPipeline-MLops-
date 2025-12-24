"""
Initializes the logger package for the Vehicle Insurance Data Pipeline MLops project.
"""
"""
Logger Module for Vehicle Insurance ML Ops Project

This module provides centralized logging configuration for the entire ML Ops pipeline.
It sets up both file-based logging with rotation and console logging for development.

Features:
- Rotating log files (5MB max, 3 backups)
- Timestamped log filenames
- Different log levels for file vs console
- Automatic log directory creation

Usage:
    Import this module to configure logging for your application.
    The logger will be automatically configured when the module is imported.
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# Constants for log configuration
LOG_DIR = 'logs'  # Directory name for storing log files
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Timestamped log filename
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB - Maximum size of each log file before rotation
BACKUP_COUNT = 3  # Number of backup log files to keep (rotates when max size reached)

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)  # Full path to logs directory
os.makedirs(log_dir_path, exist_ok=True)  # Create logs directory if it doesn't exist
log_file_path = os.path.join(log_dir_path, LOG_FILE)  # Full path to log file

def configure_logger():
    """
    Configure the root logger with rotating file handler and console handler.

    This function sets up a comprehensive logging system that:
    - Logs DEBUG level and above to rotating files
    - Logs INFO level and above to console
    - Automatically rotates log files when they reach 5MB
    - Keeps 3 backup log files
    - Uses timestamped filenames for each run

    Returns:
        None: Modifies the root logger in place

    Note:
        This function should be called once at application startup.
        Subsequent calls will add duplicate handlers.
    """
    # Create a custom logger (root logger)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set minimum logging level to DEBUG

    # Define formatter for consistent log message format
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation - for persistent logging
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=MAX_LOG_SIZE,      # Rotate when file reaches 5MB
        backupCount=BACKUP_COUNT    # Keep 3 backup files
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)  # Log all levels to file

    # Console handler - for development and debugging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)  # Only log INFO and above to console

    # Add handlers to the root logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger when this module is imported
# This ensures logging is set up automatically for the entire application
configure_logger()