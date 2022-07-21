from parent.config.configuration import Configuration
from parent.logger import logging
from parent.exception import ForestException
from parent.entity.config_entity import DataIngestionConfig, DataValidationConfig
from parent.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from parent.component.data_ingestion import DataIngestion
from parent.component.data_validation import DataValidation
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


    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)-> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                            data_ingestion_artifact=data_ingestion_artifact
                                            )
            
            # Runs the function from component file
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise ForestException(e,sys) from e


    def run_pipeline(self):
        try:
            # Data ingestion is called
            data_ingestion_artifact = self.start_data_ingestion()

            # Data validation is called
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise ForestException(e,sys) from e        