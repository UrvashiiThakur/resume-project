from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import sys, os
from dataclasses import dataclass
import pandas as pd
import numpy as np
import pickle


from src.exception import DataIngestionError,DataTransformationError
from src.logger import logging

# data  transformation
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join(os.getcwd(),'artifacts','preprocessor.pkl')

class DataTransformationConfig:
    def __init__(self):
        self.data_transformation = DataTransformationConfig()

    def get_data_transformation_obj(self):


    def initate_data_transformation(self,train_data,path,test_data):
        