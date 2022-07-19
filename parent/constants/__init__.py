import os
from datetime import datetime

# Create function to return datetime across the entire project
def create_timestamp_value():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


# Declare all constants required in the project here

# Here we are passing the entire file path for config.yaml file
ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Training pipeline related variables which are declared as key:value pairs in the config.yaml file
# We will be accessing the key:value pairs from the config.yaml file in the readconfig through these constants and not directly
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# Data Ingestion related variables which are declared as key:value pairs in the config.yaml file
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion" # This is a folder created by artifact step and is not defined in the config.yaml file, hence it doesn't have KEY in name
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_ZIP_DOWNLOAD_DIR_KEY = "zip_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_data_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"