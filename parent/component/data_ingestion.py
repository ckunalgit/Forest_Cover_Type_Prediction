# The input to each of the components in this directory will be the config files read from config_entity and the output will be artifacts as defined under artifact_entity

from tkinter import E
from parent.entity.config_entity import DataIngestionConfig
import os,sys
from parent.exception import ForestException
from parent.logger import logging

class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ForestException(e,sys) from e

# We will define separate functions for each of the below steps in data ingestion
    '''
    > Download data
    > Extract the data
    > Split raw data into train and test
    '''

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise ForestException(e,sys) from e