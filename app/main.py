#!/usr/bin/python3
from models.engine.app import app
from flask import jsonify
import os
from routes import *


@app.route("/", methods=['GET'])
def index():
    return jsonify({"data": "index page"})


@app.after_request
def apply_headers(response):
    response.headers.add("Access-Control-Expose-Headers", "X-Total-Count")
    return response


if __name__ == "__main__":
    # db.engine.echo = True
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
    print("App started")
