import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def create_directory(directory_path):
    try:
        os.makedirs(directory_path)
        logger.info(f"Directory created: {directory_path}")
    except FileExistsError:
        logger.info(f"Directory already exists: {directory_path}")
    except Exception as e:
        logger.error(f"Failed to create directory: {directory_path} - {str(e)}")
        raise

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def is_valid_file_path(file_path):
    return os.path.isfile(file_path)

def get_file_size(file_path):
    return os.path.getsize(file_path)