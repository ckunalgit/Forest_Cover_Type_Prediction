from flask import Flask
from parent.logger import logging
from parent.exception import ForestException
import sys


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    # Testing logging module
    #logging.info("We are testing logger module")

    # Testing exception
    try :
        raise Exception("Testing custom exception")
    except Exception as e:
        forest = ForestException(e,sys)
        logging.info(forest.error_message)
    return "Starting forest cover project"
    

if __name__ == "__main__":
    app.run(debug=True)