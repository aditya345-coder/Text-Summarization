import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file

    Args:
        path_to_yaml (Path): path 
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: _description_
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succesfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): the list of path of directories
        ignore (bool, optional): _description_. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    """size in KB

    Args:
        path (Path): path of file

    Returns:
        str: size in KB
    """
    size_in_KB=round(os.path.getsize(path)/1024)
    return f"~{size_in_KB} KB"