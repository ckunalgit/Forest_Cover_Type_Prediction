from parent.config.configuration import Configuration
from parent.pipeline.pipeline import Pipeline
from parent.logger import logging
from parent.exception import ForestException

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)
"""

def main():
    config = Configuration()
    config.get_data_ingestion_config()
"""    

if __name__=="__main__":
    main()