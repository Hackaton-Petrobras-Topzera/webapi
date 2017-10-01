import json

from flask import Flask, jsonify

from service.database import Dao
from service.service import GasStationService

app = Flask(__name__)


def obj_dict(obj):
    return obj.__dict__

def to_json(data):
    response = app.response_class(
        response=json.dumps(data, default=obj_dict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gasstation')
def gas_station():
    all_gas = GasStationService().select_all_gas()
    return to_json(all_gas)

@app.route('/connection/status')
def connection_status():
    dao = Dao()
    dao.connect()
    dao.close_connection()
    return jsonify(connection=True), 200


if __name__ == '__main__':
    app.run()
