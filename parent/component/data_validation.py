from parent.logger import logging
from parent.exception import ForestException
from parent.entity.config_entity import DataValidationConfig
from parent.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os,sys
import json
import pandas as pd

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

class DataValidation:

    def __init__(self, data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact # Output of data ingestion will be an input here
    ):

        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise ForestException(e,sys) from e

# This function to check if train and test files exists or not
    def is_train_test_file_exists(self):
        try:
            logging.info("Starting test and train file availability checks!!")
            is_train_file_exists = False
            is_test_file_exists = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exists = os.path.exists(train_file_path)
            is_test_file_exists = os.path.exists(test_file_path)

            is_available = is_train_file_exists and is_test_file_exists

            logging.info(f"Does Train and Test files exist? -> {is_available}")

            if not is_available:
                # Here we are taking 2 variables which will hold train and test file paths
                # The reason for this is so that the logging and exception messages are beautifully printed for the user
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file: {training_file} or Testing file: {testing_file} deos not exist"
                logging.info(message)
                raise Exception(message)
            return is_available # This is a boolean value means both files have to exist else it will return False

        except Exception as e:
            raise ForestException(e,sys) from e


    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df,test_df
        except Exception as e:
            raise ForestException(e,sys) from e

# This function will read Profile of the train and test datasets and store in a file. There should not be any data drift between train and test datasets
    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df,test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df)

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path # This is coming from config_entity.py
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)
            logging.info(f"Data drift report: {report} has been saved")
            return report
        except Exception as e:
            raise ForestException(e,sys) from e
    

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs = [DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)           
            dashboard.save(self.data_validation_config.report_page_file_path)
        except Exception as e:
            raise ForestException(e,sys) from e


# This function will validate the dataset on different parameters like number of columns and do domain check on columns
    def validate_dataset_schema(self)-> bool:
        try:
            validation_status = False
            validation_status = True
            return validation_status
        except Exception as e:
            raise ForestException(e,sys) from e

# This function will check if data drift is found or not <data drift : Change in underlying stats of the dataset>
    def is_data_drift_found(self)-> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            ###
            #Once we save the report from save_data_drift_report_page(), we will view the json dashboard to write the functionality here            
            ###

            return True
        except Exception as e:
            raise ForestException(e,sys) from e

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()
                
            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successully."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact            
        except Exception as e:
            raise ForestException(e,sys) from e
    
    def __del__(self):
        logging.info(f"{'>>'*30}Data Validation log completed.{'<<'*30} \n\n")