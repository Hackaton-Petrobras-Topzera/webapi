from flask import Flask
from flask import jsonify
import json

from model.contract import GasStation

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

    gas = GasStation(id=1, latitude=-22.929741, longitude=-43.179529)
    gas2 = GasStation(id=2, latitude=-22.929692, longitude=-43.177769, favorite=True)
    gas3 = GasStation(id=3, latitude=-22.928299, longitude=-43.179496, franchise=True)

    all_gas = [gas, gas2, gas3]
    return to_json(all_gas)


if __name__ == '__main__':
    app.run()
