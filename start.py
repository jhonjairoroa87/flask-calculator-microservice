__author__ = 'jhonjairoroa87'

import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
