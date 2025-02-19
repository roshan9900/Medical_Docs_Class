import os
import yaml 
from src.Medical_Text_Classification import logger
import json, joblib
from ensure import ensure_annotations
from box.config_box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations

def read_yaml(path_to_yaml) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded succesfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
        
        
@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
    if verbose:
        logger.info(f'created a directory at: {path}')
        
        
@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path,'w') as f:
        json.dump(data, f, indent=4)
        
    logger.info(f'json file saved at: {path}')
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f'json file loaded succesfully from: {path}')
    return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f'binary file saved at: {path}')
    
@ensure_annotations
def load_bin(path: Path) ->Any:
    data = joblib.load(path)
    logger.info(f'binary file laoded from: {path}')
    return data