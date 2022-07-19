from parent.config.configuration import Configuration
from parent.logger import logging
from parent.exception import ForestException
from parent.entity.config_entity import DataIngestionConfig
from parent.entity.artifact_entity import DataIngestionArtifact
from parent.component.data_ingestion import DataIngestion
import os,sys

class Pipeline:

    def __init__(self, config: Configuration = Configuration())-> None: # This init function takes object of Configuration class as input
        try:
            self.config = config
        except Exception as e:
            raise ForestException(e,sys) from e

    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config()) # Reads the data ingestion config parameters from Configuration class
            
            # Runs the function from component file
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise ForestException(e,sys) from e
    
    def run_pipeline(self):
        try:
            # Data ingestion will be called
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise ForestException(e,sys) from e        