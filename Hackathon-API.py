from flask import Flask
from flask import jsonify
import json

from model.contract import GasStation

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gasstation')
def hue():
    gas = GasStation()
    return json.dumps(gas.__dict__)


if __name__ == '__main__':
    app.run()
