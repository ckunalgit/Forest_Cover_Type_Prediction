from parent.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from parent.utils.utils import *
from parent.constants import *
from parent.exception import ForestException
from parent.logger import logging
import sys


class Configuration:

    def __init__(self, config_file_path = CONFIG_FILE_PATH, current_timestamp:str = CURRENT_TIMESTAMP)-> None:
        """This is the constructor function which will read the config.yaml file"""
        try:
            # We read the yaml file read function from utils folder and pass the path info here
            # This will return a dictionary which will be used in the functions below
            self.config_info = read_yaml_file(file_path = config_file_path) 
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_timestamp
        except Exception as e:
            raise ForestException(e,sys) from e


    def get_data_ignestion_config(self)-> DataIngestionConfig:
        try:
            # Storing the config info for data ingestion in a variable
            data_ingestion_config_info = self.config_info[DATA_INGESTION_CONFIG_KEY]

            # We will get the artifact directory from the training pipeline config
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp) # path is created as /parent/artifac/data_ingestion/current_time

            dataset_download_url = data_ingestion_config_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            #/parent/artifac/data_ingestion/current_time/raw_data
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_RAW_DATA_DIR_KEY]) 

            #/parent/artifac/data_ingestion/current_time/zip_data
            zip_download_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_ZIP_DOWNLOAD_DIR_KEY])

            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_train_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[DATA_INGESTION_TEST_DIR_KEY])

            # The below step is used to create a namedtuple which will hold all the above values read from the config file
            # We will be using this namedtuple in our later codes wherever data ingestion information is required
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                raw_data_dir=raw_data_dir,
                zip_download_dir=zip_download_dir,
                ingested_dir=ingested_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir
            )


            logging.info(f"Data Ingestion Config: {DataIngestionConfig}")
            return data_ingestion_config
        except Exception as e:
            raise ForestException(e,sys) from e
            


    def get_training_pipeline_config(self)-> TrainingPipelineConfig:
        try:
            # This will return us a dictionary where key = 'training_pipeline_config' from the config.yaml file. The key is passed from the constants file
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            
            # This will create a folder as /rootdir/<pipelinename>/artifact, which will contain all the project artifacts
            artifact_dir = os.path.join(ROOT_DIR, training_pipeline_config[TRAINING_PIPELINE_NAME_KEY], training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            # We will create a namedtuple where we will pass the values of the artifact directory
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Config : {training_pipeline_config}")
            return training_pipeline_config # This will return "TrainingPipelineConfig(artifact_dir = "E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\parent\artifact")
        except Exception as e:
            raise ForestException(e,sys) from e