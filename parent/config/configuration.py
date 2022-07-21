from parent.entity.artifact_entity import DataValidationArtifact
from parent.entity.config_entity import DataIngestionConfig, DataValidationConfig,TrainingPipelineConfig
from parent.utils.utils import read_yaml_file
from parent.logger import logging
import sys,os
from parent.constants import *
from parent.exception import ForestException


class Configuration:

    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_timestamp:str = CURRENT_TIMESTAMP
        ) -> None:
        """This is the constructor function which will read the config.yaml file"""
        try:
            # We read the yaml file read function from utils folder and pass the path info here
            # This will return a dictionary which will be used in the functions below            
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_timestamp
        except Exception as e:
            raise ForestException(e,sys) from e


    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
            # We will get the artifact directory from the training pipeline config            
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )

            # Storing the config info for data ingestion in a variable            
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]

            #/forestcover/artifact/data_ingestion/current_time/zip_data
            zip_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_ZIP_DOWNLOAD_DIR_KEY]
            )

            #/forestcover/artifact/data_ingestion/current_time/raw_data
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            #\forestcover\artifact\data_ingestion\current_timestamp/ingested_data_dir
            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )

            #\forestcover\artifact\data_ingestion\current_timestamp/ingested_train_dir
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )

            #\forestcover\artifact\data_ingestion\current_timestamp/ingested_test_dir
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )

            # The below step is used to create a namedtuple which will hold all the above values read from the config file
            # We will be using this namedtuple in our later codes wherever data ingestion information is required
            data_ingestion_config=DataIngestionConfig(
                dataset_download_url=dataset_download_url, 
                zip_download_dir=zip_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise ForestException(e,sys) from e

    def get_data_validation_config(self) -> DataValidationArtifact:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_VALIDATION_ARTIFACT_DIR,
                self.time_stamp
            )

            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            schema_file_path = os.path.join(ROOT_DIR,
                data_validation_config[DATA_VALIDATION_SCHEMA_DIR_KEY],
                data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
            )

            report_file_path = os.path.join(data_validation_artifact_dir,
                data_validation_config[DATA_VALIDATION_REPORT_FILE_NAME_KEY]
            )

            report_page_file_path = os.path.join(data_validation_artifact_dir,
                data_validation_config[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY]
            )

            data_validation_config=DataValidationConfig(
                schema_file_path=schema_file_path,
                report_file_path=report_file_path,
                report_page_file_path=report_page_file_path
            )

            return data_validation_config
        except Exception as e:
            raise ForestException(e,sys) from e


    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            # This will return us a dictionary where key = 'training_pipeline_config' from the config.yaml file. The key is passed from the constants file
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

            # This will create a folder as /rootdir/forestcover/artifact, which will contain all the project artifacts
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            # We will create a namedtuple where we will pass the values of the artifact directory
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise ForestException(e,sys) from e