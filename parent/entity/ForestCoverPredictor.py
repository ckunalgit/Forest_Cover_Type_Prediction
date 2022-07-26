import os
import sys

from parent.exception import ForestException
from parent.utils.utils import load_object

import pandas as pd


class ForestCoverData:

    def __init__(self,
				 Elevation: int,
				 Aspect: int,
				 Slope: int,
				 Horizontal_Distance_To_Hydrology: int,
				 Vertical_Distance_To_Hydrology: int,
				 Horizontal_Distance_To_Roadways: int,
				 Hillshade_9am: int,
				 Hillshade_Noon: int,
				 Hillshade_3pm: int,
				 Horizontal_Distance_To_Fire_Points: int,
				 Wilderness_Area1: int,
				 Wilderness_Area2: int,
				 Wilderness_Area3: int,
				 Wilderness_Area4: int,
				 Soil_Type1: int,
				 Soil_Type2: int,
				 Soil_Type3: int,
				 Soil_Type4: int,
				 Soil_Type5: int,
				 Soil_Type6: int,
				 Soil_Type7: int,
				 Soil_Type8: int,
				 Soil_Type9: int,
				 Soil_Type10: int,
				 Soil_Type11: int,
				 Soil_Type12: int,
				 Soil_Type13: int,
				 Soil_Type14: int,
				 Soil_Type15: int,
				 Soil_Type16: int,
				 Soil_Type17: int,
				 Soil_Type18: int,
				 Soil_Type19: int,
				 Soil_Type20: int,
				 Soil_Type21: int,
				 Soil_Type22: int,
				 Soil_Type23: int,
				 Soil_Type24: int,
				 Soil_Type25: int,
				 Soil_Type26: int,
				 Soil_Type27: int,
				 Soil_Type28: int,
				 Soil_Type29: int,
				 Soil_Type30: int,
				 Soil_Type31: int,
				 Soil_Type32: int,
				 Soil_Type33: int,
				 Soil_Type34: int,
				 Soil_Type35: int,
				 Soil_Type36: int,
				 Soil_Type37: int,
				 Soil_Type38: int,
				 Soil_Type39: int,
				 Soil_Type40: int,
				 Cover_Type: int = None
                 ):
        try:
            self.Elevation = Elevation
            self.Aspect = Aspect
            self.Slope = Slope
            self.Horizontal_Distance_To_Hydrology = Horizontal_Distance_To_Hydrology
            self.Vertical_Distance_To_Hydrology = Vertical_Distance_To_Hydrology
            self.Horizontal_Distance_To_Roadways = Horizontal_Distance_To_Roadways
            self.Hillshade_9am = Hillshade_9am
            self.Hillshade_Noon = Hillshade_Noon
            self.Hillshade_3pm = Hillshade_3pm
            self.Horizontal_Distance_To_Fire_Points = Horizontal_Distance_To_Fire_Points
            self.Wilderness_Area1 = Wilderness_Area1
            self.Wilderness_Area2 = Wilderness_Area2
            self.Wilderness_Area3 = Wilderness_Area3
            self.Wilderness_Area4 = Wilderness_Area4
            self.Soil_Type1 = Soil_Type1
            self.Soil_Type2 = Soil_Type2
            self.Soil_Type3 = Soil_Type3
            self.Soil_Type4 = Soil_Type4
            self.Soil_Type5 = Soil_Type5
            self.Soil_Type6 = Soil_Type6
            self.Soil_Type7 = Soil_Type7
            self.Soil_Type8 = Soil_Type8
            self.Soil_Type9 = Soil_Type9
            self.Soil_Type10 = Soil_Type10
            self.Soil_Type11 = Soil_Type11
            self.Soil_Type12 = Soil_Type12
            self.Soil_Type13 = Soil_Type13
            self.Soil_Type14 = Soil_Type14
            self.Soil_Type15 = Soil_Type15
            self.Soil_Type16 = Soil_Type16
            self.Soil_Type17 = Soil_Type17
            self.Soil_Type18 = Soil_Type18
            self.Soil_Type19 = Soil_Type19
            self.Soil_Type20 = Soil_Type20
            self.Soil_Type21 = Soil_Type21
            self.Soil_Type22 = Soil_Type22
            self.Soil_Type23 = Soil_Type23
            self.Soil_Type24 = Soil_Type24
            self.Soil_Type25 = Soil_Type25
            self.Soil_Type26 = Soil_Type26
            self.Soil_Type27 = Soil_Type27
            self.Soil_Type28 = Soil_Type28
            self.Soil_Type29 = Soil_Type29
            self.Soil_Type30 = Soil_Type30
            self.Soil_Type31 = Soil_Type31
            self.Soil_Type32 = Soil_Type32
            self.Soil_Type33 = Soil_Type33
            self.Soil_Type34 = Soil_Type34
            self.Soil_Type35 = Soil_Type35
            self.Soil_Type36 = Soil_Type36
            self.Soil_Type37 = Soil_Type37
            self.Soil_Type38 = Soil_Type38
            self.Soil_Type39 = Soil_Type39
            self.Soil_Type40 = Soil_Type40
            self.Cover_Type = Cover_Type            
        except Exception as e:
            raise ForestException(e, sys) from e

    def get_forest_cover_input_data_frame(self):

        try:
            housing_input_dict = self.get_housing_data_as_dict()
            return pd.DataFrame(housing_input_dict)
        except Exception as e:
            raise ForestException(e, sys) from e

    def get_forest_cover_data_as_dict(self):
        try:
            input_data = {
				"Elevation": [self.Elevation],
				"Aspect": [self.Aspect],
				"Slope": [self.Slope],
				"Horizontal_Distance_To_Hydrology": [self.Horizontal_Distance_To_Hydrology],
				"Vertical_Distance_To_Hydrology": [self.Vertical_Distance_To_Hydrology],
				"Horizontal_Distance_To_Roadways": [self.Horizontal_Distance_To_Roadways],
				"Hillshade_9am": [self.Hillshade_9am],
				"Hillshade_Noon": [self.Hillshade_Noon],
				"Hillshade_3pm": [self.Hillshade_3pm],
				"Horizontal_Distance_To_Fire_Points": [self.Horizontal_Distance_To_Fire_Points],
				"Wilderness_Area1": [self.Wilderness_Area1],
				"Wilderness_Area2": [self.Wilderness_Area2],
				"Wilderness_Area3": [self.Wilderness_Area3],
				"Wilderness_Area4": [self.Wilderness_Area4],
				"Soil_Type1": [self.Soil_Type1],
				"Soil_Type2": [self.Soil_Type2],
				"Soil_Type3": [self.Soil_Type3],
				"Soil_Type4": [self.Soil_Type4],
				"Soil_Type5": [self.Soil_Type5],
				"Soil_Type6": [self.Soil_Type6],
				"Soil_Type7": [self.Soil_Type7],
				"Soil_Type8": [self.Soil_Type8],
				"Soil_Type9": [self.Soil_Type9],
				"Soil_Type10": [self.Soil_Type10],
				"Soil_Type11": [self.Soil_Type11],
				"Soil_Type12": [self.Soil_Type12],
				"Soil_Type13": [self.Soil_Type13],
				"Soil_Type14": [self.Soil_Type14],
				"Soil_Type15": [self.Soil_Type15],
				"Soil_Type16": [self.Soil_Type16],
				"Soil_Type17": [self.Soil_Type17],
				"Soil_Type18": [self.Soil_Type18],
				"Soil_Type19": [self.Soil_Type19],
				"Soil_Type20": [self.Soil_Type20],
				"Soil_Type21": [self.Soil_Type21],
				"Soil_Type22": [self.Soil_Type22],
				"Soil_Type23": [self.Soil_Type23],
				"Soil_Type24": [self.Soil_Type24],
				"Soil_Type25": [self.Soil_Type25],
				"Soil_Type26": [self.Soil_Type26],
				"Soil_Type27": [self.Soil_Type27],
				"Soil_Type28": [self.Soil_Type28],
				"Soil_Type29": [self.Soil_Type29],
				"Soil_Type30": [self.Soil_Type30],
				"Soil_Type31": [self.Soil_Type31],
				"Soil_Type32": [self.Soil_Type32],
				"Soil_Type33": [self.Soil_Type33],
				"Soil_Type34": [self.Soil_Type34],
				"Soil_Type35": [self.Soil_Type35],
				"Soil_Type36": [self.Soil_Type36],
				"Soil_Type37": [self.Soil_Type37],
				"Soil_Type38": [self.Soil_Type38],
				"Soil_Type39": [self.Soil_Type39],
				"Soil_Type40": [self.Soil_Type40]}
            return input_data
        except Exception as e:
            raise ForestException(e, sys)


class ForestCoverPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise ForestException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise ForestException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            cover_type = model.predict(X)
            return cover_type
        except Exception as e:
            raise ForestException(e, sys) from e