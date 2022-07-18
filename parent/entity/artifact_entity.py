from collections import namedtuple

# Create namedtuple for each of the artifacts created at each step of the pipeline
DataIngestionArtifact = namedtuple("DataIngestionArtifact",
    ["train_file_path",
    "test_file_path",
    "is_ingested",
    "message"])