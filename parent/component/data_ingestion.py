from parent.entity.config_entity import DataIngestionConfig
import sys,os
from parent.exception import ForestException
from parent.logger import logging
from parent.entity.artifact_entity import DataIngestionArtifact
#import tarfile
import zipfile
import numpy as np
from six.moves import urllib
import pandas as pd
#from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config
            print(self.data_ingestion_config.dataset_download_url)

        except Exception as e:
            raise ForestException(e,sys)
    
# We will define separate functions for each of the below steps in data ingestion
    '''
    > Download data
    > Extract the data
    > Split raw data into train and test
    '''


    def download_forest_data(self,) -> str:
        try:
            # This is coming from the configuration class in config folder
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            zip_download_dir = self.data_ingestion_config.zip_download_dir
            
            os.makedirs(zip_download_dir,exist_ok=True)

            #housing_file_name = os.path.basename(download_url)

            # Getting the filename from the kaggle website
            # Our download url contains many characters after zip, so we need to separate the filename
            basefile = os.path.basename(download_url)
            forest_file_name = basefile.split('?')[0]

            zip_file_path = os.path.join(zip_download_dir, forest_file_name)

            logging.info(f"Downloading file from :[{download_url}] into :[{zip_file_path}]")
            urllib.request.urlretrieve(download_url, zip_file_path)
            logging.info(f"File :[{zip_file_path}] has been downloaded successfully.")
            return zip_file_path

        except Exception as e:
            raise ForestException(e,sys) from e

    def extract_zip_file(self,zip_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting zip file: [{zip_file_path}] into dir: [{raw_data_dir}]")
 #           with tarfile.open(zip_file_path) as housing_tgz_file_obj:
 #               housing_tgz_file_obj.extractall(path=raw_data_dir)

             # The zipfile path is passed to this function when its called in initiate_data_ingestion
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)
            logging.info(f"Extraction completed")

        except Exception as e:
            raise ForestException(e,sys) from e
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            # Getting the raw data file from the raw_data_directory
            file_name = os.listdir(raw_data_dir)[0]
            forest_file_path = os.path.join(raw_data_dir,file_name)
#            housing_file_path = os.path.join(raw_data_dir,file_name)

            logging.info(f"Reading csv file: [{forest_file_path}]")
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

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise ForestException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            zip_file_path =  self.download_forest_data()
            self.extract_zip_file(zip_file_path=zip_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise ForestException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")
