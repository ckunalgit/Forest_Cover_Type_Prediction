from collections import namedtuple

# This namedtuple will read the config.yaml file and pass it onto the config.py file in config folder
DataIngestionConfig = namedtuple("DataIngestionConfig",
    ["dataset_download_url",
    "zip_download_dir",
    "raw_data_dir",    
    "ingested_train_dir",
    "ingested_test_dir"])

# This namedtuple will have the pipeline name and artifact dir
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
    ["artifact_dir"])