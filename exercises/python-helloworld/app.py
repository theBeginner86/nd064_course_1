import json
import logging

from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format="{{%(asctime)s}}, {{%(levelname)s}}, {{%(message)s}} endpoint reached successfully.")


@app.route("/")
def hello():
    response_name = str(request.url_rule)
    logging.info(response_name)

    return "Hello World!"


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    response_name = str(request.url_rule)

    if response_name == '/status':
        logging.info(response_name)

    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}, "status": "success", "code": 0}),
        status=200,
        mimetype='application/json'
    )
    response_name = str(request.url_rule)

    if response_name == '/metrics':
        logging.info(response_name)

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
