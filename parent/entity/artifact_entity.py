from collections import namedtuple

# Create namedtuple for each of the artifacts created at each step of the pipeline
DataIngestionArtifact = namedtuple("DataIngestionArtifact",
    ["train_file_path",
    "test_file_path",
    "is_ingested",
    "message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
    ["schema_file_path",
    "report_file_path",
    "report_page_file_path",
    "is_validated",
    "message"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",
    ["transformed_train_file_path",
    "transformed_test_file_path",
    "preprocessed_object_file_path",
    "is_transformed",
    "message"])

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",
    ["trained_model_file_path",
    "train_accuracy",
    "test_accuracy",
    "model_accuracy",
    "is_trained",
    "message"])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact",
    ["is_model_accepted",
    "evaluated_model_path"])

ModelPusherArtifact = namedtuple("ModelPusherArtifact",
    ["is_model_pusher",
    "export_model_file_path"])