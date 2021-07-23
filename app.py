from flask import json
from flask import Flask
import logging
from datetime import datetime
app = Flask(__name__)



@app.route("/")
def hello():
    app.logger.info("{}, {} endpoint was reached".format(datetime.now(), 'root'))
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info("{}, {} endpoint was reached".format(datetime.now(), 'status'))

    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info("{}, {} endpoint was reached".format(datetime.now(), 'metrics'))

    return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="app.log",
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
    app.run(host='0.0.0.0')
