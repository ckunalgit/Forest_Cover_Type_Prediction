from collections import namedtuple

# This namedtuple will read the config.yaml file and pass it onto the config.py file in config folder
DataIngestionConfig = namedtuple("DataIngestionConfig",
    ["dataset_download_url",
    "zip_download_dir",
    "raw_data_dir",    
    "ingested_train_dir",
    "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",
    ["schema_file_path",
    "report_file_path",    
    "report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",
    ["transformed_train_dir",
    "transformed_test_dir",
    "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",
    ["trained_model_file_path",
    "base_accuracy",
    "model_config_file_path"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
    ["model_evaluation_file_path",
    "time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",
    ["export_dir_path"])    

# This namedtuple will have the pipeline name and artifact dir
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
    ["artifact_dir"])