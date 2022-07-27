from parent.pipeline.pipeline import Pipeline
from parent.logger import logging
from parent.exception import ForestException
from parent.config.configuration import Configuration
from parent.component.data_transformation import DataTransformation
import pickle
import numpy as np

from parent.entity.ForestCoverPredictor import ForestCoverData, ForestCoverPredictor
from parent.constants import *

def main():
    try:
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        #pipeline.run_pipeline()
        
        #data_ingestion_config = Configuration().get_data_ingestion_config()
        #data_validation_config = Configuration().get_data_validation_config()

        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)

        #schema_file_path = r"E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\config\schema.yaml"
        #file_path = r"E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\forestcover\artifact\data_ingestion\2022-07-21-22-15-29\ingested_data\train\covtype.csv"
        #df = DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
        SAVED_MODELS_DIR_NAME = "saved_models"
        MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)

        forestcover_data = ForestCoverData(Elevation = 100,
                                        Aspect = 180,
                                        Slope = 212,
                                        Horizontal_Distance_To_Hydrology = 0,
                                        Vertical_Distance_To_Hydrology = 0,
                                        Horizontal_Distance_To_Roadways = 0,
                                        Hillshade_9am = 0,
                                        Hillshade_Noon = 192,
                                        Hillshade_3pm = 123,
                                        Horizontal_Distance_To_Fire_Points = 2200,
                                        Wilderness_Area1 = 0,
                                        Wilderness_Area2 = 0,
                                        Wilderness_Area3 = 1,
                                        Wilderness_Area4 = 0,
                                        Soil_Type1 = 0,
                                        Soil_Type2 = 0,
                                        Soil_Type3 = 0,
                                        Soil_Type4 = 0,
                                        Soil_Type5 = 0,
                                        Soil_Type6 = 0,
                                        Soil_Type7 = 0,
                                        Soil_Type8 = 0,
                                        Soil_Type9 = 0,
                                        Soil_Type10 = 0,
                                        Soil_Type11 = 0,
                                        Soil_Type12 = 0,
                                        Soil_Type13 = 0,
                                        Soil_Type14 = 0,
                                        Soil_Type15 = 0,
                                        Soil_Type16 = 0,
                                        Soil_Type17 = 0,
                                        Soil_Type18 = 0,
                                        Soil_Type19 = 0,
                                        Soil_Type20 = 0,
                                        Soil_Type21 = 0,
                                        Soil_Type22 = 0,
                                        Soil_Type23 = 0,
                                        Soil_Type24 = 0,
                                        Soil_Type25 = 0,
                                        Soil_Type26 = 0,
                                        Soil_Type27 = 0,
                                        Soil_Type28 = 0,
                                        Soil_Type29 = 0,
                                        Soil_Type30 = 0,
                                        Soil_Type31 = 0,
                                        Soil_Type32 = 0,
                                        Soil_Type33 = 0,
                                        Soil_Type34 = 0,
                                        Soil_Type35 = 0,
                                        Soil_Type36 = 0,
                                        Soil_Type37 = 0,
                                        Soil_Type38 = 1,
                                        Soil_Type39 = 0,
                                        Soil_Type40 = 0
                                        )
        forestcover_df = forestcover_data.get_forest_cover_input_data_frame()
        forest_cover_predictor = ForestCoverPredictor(model_dir=MODEL_DIR)
        Cover_Type = forest_cover_predictor.predict(X=forestcover_df)
        logging.info(Cover_Type)
#        with open(r"E:\ineuron\vs\projects\Forest_Cover_Type_Prediction\saved_models\20220727114802\model.pkl", "rb") as f:
#            rfc = pickle.load(f)
#        Cover_type = rfc.predict([[3351,206,27,726,124,3813,192,252,180,2271,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
#        print(Cover_type)

    except Exception as e:
        logging.error(f"{e}")
        print(e)
  

if __name__=="__main__":
    main()