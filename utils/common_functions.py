import os
import pandas
from src.logger import get_logger
from src.exception import CustomException
import yaml
import pandas as pd

logger = get_logger(__name__)

def read_yaml(file_path:str):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"YAML file not found at {file_path}")
        
        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully from {file_path}")
            return config
        
    except Exception as e:
        logger.error(f"Error reading YAML file")
        raise CustomException("Failed to read YAML file", e)