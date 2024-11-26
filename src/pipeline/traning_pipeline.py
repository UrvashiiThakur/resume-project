import os
import sys
from src.logger import logging
from src.exception import DataIngestionError
import pandas as pd

from src.components.data_ingesttion import DataIngestion

if __name__=='__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initate_data_ingestion()
    train_data_path(), test_data_path()