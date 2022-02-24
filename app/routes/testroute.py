from flask import jsonify
from models.engine.app import app


@app.route('/testroute', methods=['GET'])
def getTestData():
    return jsonify({"data": "Here's some test data"})
