from parent.pipeline.pipeline import Pipeline
from parent.logger import logging
from parent.exception import ForestException
from parent.config.configuration import Configuration

def main():
    try:
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        
        #data_ingestion_config = Configuration().get_data_ingestion_config()
        #data_validation_config = Configuration().get_data_validation_config()

        data_transformation_config = Configuration().get_data_transformation_config()
        print(data_transformation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)
  

if __name__=="__main__":
    main()