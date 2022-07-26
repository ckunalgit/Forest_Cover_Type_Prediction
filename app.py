from flask import Flask, request
import sys

import pip
from parent.utils.utils import read_yaml_file, write_yaml_file
from matplotlib.style import context
from parent.logger import logging
from parent.exception import ForestException, ForestException
import os, sys
import json
from parent.config.configuration import Configuration
from parent.constants import CONFIG_DIR, get_current_time_stamp
from parent.pipeline.pipeline import Pipeline
from parent.entity.ForestCoverPredictor import ForestCoverPredictor, ForestCoverData
from flask import send_file, abort, render_template


ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = "logs"
PIPELINE_FOLDER_NAME = "forestcover"
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, "model.yaml")
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)


from parent.logger import get_log_dataframe

FOREST_COVER_DATA_KEY = "forest_cover_data"
COVER_TYPE_VALUE_KEY = "Cover_Type"

app = Flask(__name__)


@app.route('/artifact', defaults={'req_path': 'forestcover'})
@app.route('/artifact/<path:req_path>')
def render_artifact_dir(req_path):
    os.makedirs("forestcover", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        if ".html" in abs_path:
            with open(abs_path, "r", encoding="utf-8") as file:
                content = ''
                for line in file.readlines():
                    content = f"{content}{line}"
                return content
        return send_file(abs_path)

    # Show directory contents
    files = {os.path.join(abs_path, file_name): file_name for file_name in os.listdir(abs_path) if
             "artifact" in os.path.join(abs_path, file_name)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('files.html', result=result)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)


@app.route('/view_experiment_hist', methods=['GET', 'POST'])
def view_experiment_history():
    experiment_df = Pipeline.get_experiments_status()
    context = {
        "experiment": experiment_df.to_html(classes='table table-striped col-12')
    }
    return render_template('experiment_history.html', context=context)


@app.route('/train', methods=['GET', 'POST'])
def train():
    message = ""
    pipeline = Pipeline(config=Configuration(current_time_stamp=get_current_time_stamp()))
    if not Pipeline.experiment.running_status:
        message = "Training started."
        pipeline.start()
    else:
        message = "Training is already in progress."
    context = {
        "experiment": pipeline.get_experiments_status().to_html(classes='table table-striped col-12'),
        "message": message
    }
    return render_template('train.html', context=context)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        FOREST_COVER_DATA_KEY: None,
        COVER_TYPE_VALUE_KEY: None
    }

    if request.method == 'POST':
        Elevation = int(request.form['Elevation'])
        Aspect = int(request.form['Aspect'])
        Slope = int(request.form['Slope'])
        Horizontal_Distance_To_Hydrology = int(request.form['Horizontal_Distance_To_Hydrology'])
        Vertical_Distance_To_Hydrology = int(request.form['Vertical_Distance_To_Hydrology'])
        Horizontal_Distance_To_Roadways = int(request.form['Horizontal_Distance_To_Roadways'])
        Hillshade_9am = int(request.form['Hillshade_9am'])
        Hillshade_Noon = float(request.form['Hillshade_Noon'])
        Hillshade_3pm = int(request.form['Hillshade_3pm'])

        Horizontal_Distance_To_Fire_Points = int(request.form['Horizontal_Distance_To_Fire_Points'])
        Wilderness_Area1 = int(request.form['Wilderness_Area1'])
        Wilderness_Area2 = int(request.form['Wilderness_Area2'])
        Wilderness_Area3 = int(request.form['Wilderness_Area3'])
        Wilderness_Area4 = int(request.form['Wilderness_Area4'])
        Soil_Type1 = int(request.form['Soil_Type1'])
        Soil_Type2 = int(request.form['Soil_Type2'])
        Soil_Type3 = int(request.form['Soil_Type3'])
        Soil_Type4 = int(request.form['Soil_Type4'])
        Soil_Type5 = int(request.form['Soil_Type5'])
        Soil_Type6 = int(request.form['Soil_Type6'])
        Soil_Type7 = int(request.form['Soil_Type7'])
        Soil_Type8 = int(request.form['Soil_Type8'])
        Soil_Type9 = int(request.form['Soil_Type9'])
        Soil_Type10 = int(request.form['Soil_Type10'])
        Soil_Type11 = int(request.form['Soil_Type11'])        
        Soil_Type12 = int(request.form['Soil_Type12'])
        Soil_Type13 = int(request.form['Soil_Type13'])
        Soil_Type14 = int(request.form['Soil_Type14'])
        Soil_Type15 = int(request.form['Soil_Type15'])
        Soil_Type16 = int(request.form['Soil_Type16'])
        Soil_Type17 = int(request.form['Soil_Type17'])
        Soil_Type18 = int(request.form['Soil_Type18'])
        Soil_Type19 = int(request.form['Soil_Type19'])
        Soil_Type20 = int(request.form['Soil_Type20'])
        Soil_Type21 = int(request.form['Soil_Type21'])
        Soil_Type22 = int(request.form['Soil_Type22'])
        Soil_Type23 = int(request.form['Soil_Type23'])
        Soil_Type24 = int(request.form['Soil_Type24'])
        Soil_Type25 = int(request.form['Soil_Type25'])
        Soil_Type26 = int(request.form['Soil_Type26'])
        Soil_Type27 = int(request.form['Soil_Type27'])
        Soil_Type28 = int(request.form['Soil_Type28'])                                                
        Soil_Type29 = int(request.form['Soil_Type29'])
        Soil_Type30 = int(request.form['Soil_Type30'])
        Soil_Type31 = int(request.form['Soil_Type31'])
        Soil_Type32 = int(request.form['Soil_Type32'])
        Soil_Type33 = int(request.form['Soil_Type33'])
        Soil_Type34 = int(request.form['Soil_Type34'])
        Soil_Type35 = int(request.form['Soil_Type35'])
        Soil_Type36 = int(request.form['Soil_Type36'])
        Soil_Type37 = int(request.form['Soil_Type37'])
        Soil_Type38 = int(request.form['Soil_Type38'])
        Soil_Type39 = int(request.form['Soil_Type39'])
        Soil_Type40 = int(request.form['Soil_Type40'])                                                

        forestcover_data = ForestCoverData(Elevation = Elevation,
                                    Aspect = Aspect,
									Slope = Slope,
									Horizontal_Distance_To_Hydrology = Horizontal_Distance_To_Hydrology,
									Vertical_Distance_To_Hydrology = Vertical_Distance_To_Hydrology,
									Horizontal_Distance_To_Roadways = Horizontal_Distance_To_Roadways,
									Hillshade_9am = Hillshade_9am,
									Hillshade_Noon = Hillshade_Noon,
									Hillshade_3pm = Hillshade_3pm,
									Horizontal_Distance_To_Fire_Points = Horizontal_Distance_To_Fire_Points,
									Wilderness_Area1 = Wilderness_Area1,
									Wilderness_Area2 = Wilderness_Area2,
									Wilderness_Area3 = Wilderness_Area3,
									Wilderness_Area4 = Wilderness_Area4,
									Soil_Type1 = Soil_Type1,
									Soil_Type2 = Soil_Type2,
									Soil_Type3 = Soil_Type3,
									Soil_Type4 = Soil_Type4,
									Soil_Type5 = Soil_Type5,
									Soil_Type6 = Soil_Type6,
									Soil_Type7 = Soil_Type7,
									Soil_Type8 = Soil_Type8,
									Soil_Type9 = Soil_Type9,
									Soil_Type10 = Soil_Type10,
									Soil_Type11 = Soil_Type11,
									Soil_Type12 = Soil_Type12,
									Soil_Type13 = Soil_Type13,
									Soil_Type14 = Soil_Type14,
									Soil_Type15 = Soil_Type15,
									Soil_Type16 = Soil_Type16,
									Soil_Type17 = Soil_Type17,
									Soil_Type18 = Soil_Type18,
									Soil_Type19 = Soil_Type19,
									Soil_Type20 = Soil_Type20,
									Soil_Type21 = Soil_Type21,
									Soil_Type22 = Soil_Type22,
									Soil_Type23 = Soil_Type23,
									Soil_Type24 = Soil_Type24,
									Soil_Type25 = Soil_Type25,
									Soil_Type26 = Soil_Type26,
									Soil_Type27 = Soil_Type27,
									Soil_Type28 = Soil_Type28,
									Soil_Type29 = Soil_Type29,
									Soil_Type30 = Soil_Type30,
									Soil_Type31 = Soil_Type31,
									Soil_Type32 = Soil_Type32,
									Soil_Type33 = Soil_Type33,
									Soil_Type34 = Soil_Type34,
									Soil_Type35 = Soil_Type35,
									Soil_Type36 = Soil_Type36,
									Soil_Type37 = Soil_Type37,
									Soil_Type38 = Soil_Type38,
									Soil_Type39 = Soil_Type39,
									Soil_Type40 = Soil_Type40
                                   )
        forestcover_df = forestcover_data.get_housing_input_data_frame()
        forest_cover_predictor = ForestCoverPredictor(model_dir=MODEL_DIR)
        cover_type = forest_cover_predictor.predict(X=forestcover_df)
        context = {
            FOREST_COVER_DATA_KEY: forestcover_data.get_housing_data_as_dict(),
            COVER_TYPE_VALUE_KEY: cover_type,
        }
        return render_template('predict.html', context=context)
    return render_template("predict.html", context=context)


@app.route('/saved_models', defaults={'req_path': 'saved_models'})
@app.route('/saved_models/<path:req_path>')
def saved_models_dir(req_path):
    os.makedirs("saved_models", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = {os.path.join(abs_path, file): file for file in os.listdir(abs_path)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('saved_models_files.html', result=result)


@app.route("/update_model_config", methods=['GET', 'POST'])
def update_model_config():
    try:
        if request.method == 'POST':
            model_config = request.form['new_model_config']
            model_config = model_config.replace("'", '"')
            print(model_config)
            model_config = json.loads(model_config)

            write_yaml_file(file_path=MODEL_CONFIG_FILE_PATH, data=model_config)

        model_config = read_yaml_file(file_path=MODEL_CONFIG_FILE_PATH)
        return render_template('update_model.html', result={"model_config": model_config})

    except  Exception as e:
        logging.exception(e)
        return str(e)


@app.route(f'/logs', defaults={'req_path': f'{LOG_FOLDER_NAME}'})
@app.route(f'/{LOG_FOLDER_NAME}/<path:req_path>')
def render_log_dir(req_path):
    os.makedirs(LOG_FOLDER_NAME, exist_ok=True)
    # Joining the base and the requested path
    logging.info(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        log_df = get_log_dataframe(abs_path)
        context = {"log": log_df.to_html(classes="table-striped", index=False)}
        return render_template('log.html', context=context)

    # Show directory contents
    files = {os.path.join(abs_path, file): file for file in os.listdir(abs_path)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('log_files.html', result=result)


if __name__ == "__main__":
    app.run()
