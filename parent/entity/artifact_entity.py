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