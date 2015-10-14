__author__ = 'jhonjairoroa87'

import os
from flask import Flask, request
from flask.ext.jsonpify import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "is working :)"


@app.route("/add")
def add():
    try:
        first_number = int(request.args.get('a'))
        second_number = int(request.args.get('b'))
        return jsonify({'result': first_number + second_number})
    except Exception as e:
        return "There was an error" + str(e)


@app.route("/subtract")
def subtract():
    try:
        first_number = int(request.args.get('a'))
        second_number = int(request.args.get('b'))
        return jsonify({'result': first_number - second_number})
    except Exception as e:
        return "There was an error" + str(e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
