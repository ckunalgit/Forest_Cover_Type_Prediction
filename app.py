from flask import Flask
from parent.logger import logging


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    # Testing logging module
    logging.info("We are testing logger module")
    return "Starting forest cover project"

if __name__ == "__main__":
    app.run(debug=True)