from collections import namedtuple

# This namedtuple will read the config.yaml file and pass it onto the config.py file in config folder
DataIngestionConfig = namedtuple("DataIngestionConfig",
    ["dataset_download_url",
    "raw_data_dir",
    "zip_download_dir",
    "ingested_data_dir",
    "ingested_train_dir",
    "ingested_test_dir"])

# This namedtuple will have the pipeline name and artifact dir
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
    ["artifact_dir"])