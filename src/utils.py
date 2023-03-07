import logging
from pathlib import Path 
import sys

def init_loger(filename):
    handlers = [logging.StreamHandler(sys.stdout)]
    if filename is not None: 
        path_dir = Path(filename).parents[0]
        if not path_dir.is_dir():
            path_dir.mkdir(parents=True)
        handlers.append(logging.FileHandler(filename=filename))

    logging.basicConfig(
        datefmt="%m/%d/%Y %H:%M:%S", 
        level=logging.INFO, 
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s", 
        handlers=handlers
    )


def save_to_csv(output_path, df):
    path_dir = Path(output_path).parents[0]
    if not path_dir.is_dir():
        path_dir.mkdir(parents=True)
    df.to_csv(output_path, index=False)