import json

from flask import Flask, jsonify
from flask.ext.cors import CORS, cross_origin

from service.database import Dao
from service.service import GasStationService, ProductService, OrderService

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
@cross_origin()
def hello_world():
    return 'Hello World!'


@app.route('/gasstation')
@cross_origin()
def gas_station():
    all_gas = GasStationService().select_all_gas()
    return to_json(all_gas)


@app.route('/products/all')
@cross_origin()
def get_all_products():
    products = ProductService().select_all()
    return to_json(products)


@app.route('/products/<id>')
@cross_origin()
def get_product_by_id(id):
    product = ProductService().find_by_id(int(id))
    return to_json(product)


@app.route('/products/<id>/arrangements')
@cross_origin()
def get_only_arrangements(id):
    product = ProductService().search_only_arrangement(int(id))
    return to_json(product)


@app.route('/connection/status')
@cross_origin()
def connection_status():
    dao = Dao()
    dao.connect()
    dao.close_connection()
    return jsonify(connection=True), 200


@app.route('/orders/opened')
@cross_origin()
def get_all_opened_orders():
    orders = OrderService().select_opened_orders()
    return to_json(orders)

# Not working
@app.route('/order', methods=['POST'])
def add_order():
    OrderService().order_product();
    return jsonify(success="Ok")


if __name__ == '__main__':
    app.run()
