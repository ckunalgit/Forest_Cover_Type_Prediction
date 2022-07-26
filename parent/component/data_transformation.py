from parent.logger import logging
from parent.exception import ForestException
from parent.entity.config_entity import DataTransformationConfig
from parent.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
from parent.utils.utils import read_yaml_file, save_numpy_array_data, save_object, load_data
from parent.constants import *
import os,sys
import pandas as pd
import numpy as np
from sklearn import preprocessing

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler


class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig,
                        data_ingestion_artifact: DataIngestionArtifact,
                        data_validation_artifact: DataValidationArtifact
                ):

        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise ForestException(e,sys) from e
    
   
    def get_data_transformer_object(self)-> ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path
            dataset_schema = read_yaml_file(file_path = schema_file_path)

            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]
            categorical_columns = dataset_schema[CATEGORICAL_COLUMN_KEY]

            # Now we will create the pipelines for the 2 types of columns
            # This has been tested in EDA

            numerical_pipeline = Pipeline(steps = [
                ("imputer",SimpleImputer()),
                ("scaling",MinMaxScaler())
                ])


            categorical_pipeline = Pipeline(steps = [
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ])

            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            preprocessing = ColumnTransformer([
                ('numerical',numerical_pipeline,numerical_columns),
                ('categorical',categorical_pipeline,categorical_columns)
                ])
            
            return preprocessing

        except Exception as e:
            raise ForestException(e,sys) from e

    
    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            logging.info(f"Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            logging.info(f"Obtaining training and testing file paths")
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            schema_file_path = self.data_validation_artifact.schema_file_path
            
            logging.info(f"Loading Training and Test data as a pandas dataframe")
            train_df = load_data(file_path=train_file_path, schema_file_path=schema_file_path)
            test_df = load_data(file_path=test_file_path, schema_file_path=schema_file_path)
            
            schema = read_yaml_file(file_path=schema_file_path)

            target_column_name = schema[TARGET_COLUMN_NAME_KEY]

            logging.info(f"Splitting train and test dataframes as dependent and independent features")
            input_feature_train_df = train_df.drop([target_column_name], axis = 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop([target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on train and test dataframes")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df) # Add y=None here if execution fails
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            transformed_train_dir = self.data_transformation_config.transformed_train_dir
            transformed_test_dir = self.data_transformation_config.transformed_test_dir

            # When making predictions, the filename will be in .csv, but our model will get an array as inpur, so we are typecasting it
            train_file_name = os.path.basename(train_file_path).replace(".csv",".npz")
            test_file_name = os.path.basename(test_file_path).replace(".csv",".npz")

            transformed_train_file_path = os.path.join(transformed_train_dir, train_file_name)
            transformed_test_file_path = os.path.join(transformed_test_dir, test_file_name)
            
            # Calling save array from utils          
            logging.info(f"Saving transformed train and test arrays")  
            save_numpy_array_data(file_path = transformed_train_file_path, array = train_arr)
            save_numpy_array_data(file_path = transformed_test_file_path, array = test_arr)

            logging.info(f"Saving preprocessing object")
            preprocessed_object_file_path = self.data_transformation_config.preprocessed_object_file_path
            save_object(file_path = preprocessed_object_file_path, obj=preprocessing_obj)

            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path=transformed_train_file_path,
                transformed_test_file_path=transformed_test_file_path,
                preprocessed_object_file_path=preprocessed_object_file_path,
                is_transformed=True,
                message="Data Transformation successfull!!"
            )

            logging.info(f"Data Transformation Artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise ForestException(e,sys) from e