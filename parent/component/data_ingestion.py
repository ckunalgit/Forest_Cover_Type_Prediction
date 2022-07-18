# The input to each of the components in this directory will be the config files read from config_entity and the output will be artifacts as defined under artifact_entity

from tkinter import E
from parent.entity.config_entity import DataIngestionConfig
from parent.entity.artifact_entity import DataIngestionArtifact
import os,sys
from parent.exception import ForestException
from parent.logger import logging
from six.moves import urllib
import os
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*10}Data Ingestion log started.{'<<'*10} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ForestException(e,sys) from e

# We will define separate functions for each of the below steps in data ingestion
    '''
    > Download data
    > Extract the data
    > Split raw data into train and test
    '''

    def download_raw_data(self)-> str:
        try:
            # This is coming from the configuration class in config folder
            download_url = self.data_ingestion_config.dataset_download_url
            zip_download_dir = self.data_ingestion_config.zip_download_dir

            if os.path.exists(zip_download_dir):
                os.remove(zip_download_dir)
            os.makedirs(zip_download_dir,exist_ok=True)

            # Getting the filename from the kaggle website
            # Our download url contains many characters after zip, so we need to separate the filename
            basefile = os.path.basename(download_url)
            forest_file_name = basefile.split('?')[0]

            # Zip file download path
            zip_file_path = os.path.join(zip_download_dir,forest_file_name)

            # This will download the file and accepts 2 arguments
            urllib.request.urlretrieve(download_url, zip_download_dir)

            logging.info("Downloading zip file successful!!")
            return zip_file_path

        except Exception as e:
            raise ForestException(e,sys) from e


    def extract_zip_file(self,zip_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove()
            os.makedirs(raw_data_dir,exist_ok=True)

            # The zipfile path is passed to this function when its called in initiate_data_ingestion
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)
            logging.info(f"Zip file has been successfully extracted to {raw_data_dir}!!")
        except Exception as e:
            raise ForestException(e,sys) from e


    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config

            # Getting the raw data file from the raw_data_directory
            file_name = os.listdir(raw_data_dir)[0]
            forest_file_path = os.path.join(raw_data_dir,file_name)

            # Now we will read the data from the .csv file
            forest_dataframe = pd.read_csv(forest_file_path)

            # We are defining independent and dependent variables from the dataframe
            x = forest_dataframe.drop(columns = 'Cover_Type')
            y = forest_dataframe['Cover_Type']

            x_train = None
            x_test = None

            # Now doing the train_test_split. We will have 25% data in train dataset and 75% in test dataset
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.75, random_state=42, stratify = y)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)

            if x_train is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                x_train.to_csv(train_file_path, index=False)

            if x_test is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                x_test.to_csv(test_file_path, index=False)

            # Now we will create the output of the dataingestion component in the pipeline
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                    test_file_path=test_file_path,
                                    is_ingested = "True",
                                    message = "Data Ingestion completed successfully!!")

            logging.info("Train and test datasets created!!")          
            return data_ingestion_artifact

        except Exception as e:
            raise ForestException(e,sys) from e
        pass

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            zip_file_path = self.download_raw_data

            self.extract_zip_file(zip_file_path=zip_file_path)

            return self.split_data_as_train_test()
        except Exception as e:
            raise ForestException(e,sys) from e

# This is destructor method
    def __del__():
        logging.info(f"{'>>'*10}Data Ingestion log completed.{'<<'*10} \n\n")