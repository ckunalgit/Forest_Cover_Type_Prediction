from parent.pipeline.pipeline import Pipeline
from parent.logger import logging
from parent.exception import ForestException
from parent.config.configuration import Configuration
from parent.component.data_transformation import DataTransformation

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        
        #data_ingestion_config = Configuration().get_data_ingestion_config()
        #data_validation_config = Configuration().get_data_validation_config()

        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)

        #schema_file_path = r"E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\config\schema.yaml"
        #file_path = r"E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\forestcover\artifact\data_ingestion\2022-07-21-22-15-29\ingested_data\train\covtype.csv"
        #df = DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
    except Exception as e:
        logging.error(f"{e}")
        print(e)
  

if __name__=="__main__":
    main()