import os
import ast
from pymongo import MongoClient
from flask import request, jsonify
import datetime

from model.contract import Product


class Dao:
    def connect(self):
        # self.client = MongoClient('localhost', 27017)
        self.client = MongoClient(os.environ['MONGO'])
        # self.client = MongoClient("mongodb://topzera:HackatopPetro@ds155934.mlab.com:55934/hackathon_br")

    def close_connection(self):
        self.client.close()

    def get_database(self):
        return self.client['hackathon_br']


class LocationDao(Dao):
    def get_location_collection(self):
        self.connect()
        gas_station_database = self.get_database()
        return gas_station_database['gas_station']

    def get_all_gas_stations_from_rj(self):
        collection = self.get_location_collection()

        result = []

        all_gas_station_from_rj = collection.find({
            "state": "RJ",
            "latitude": {"$ne": "NULL"},
            "longitude": {"$type": "number"}
        }, {
            "latitude": 1,
            "longitude": 1,
            "id": 1,
            "fantasy_name": 1,
            "name": 1
        }
        )

        for location in all_gas_station_from_rj:
            location.pop("_id")
            result.append(location)

        return result


class ProductDao(Dao):
    def get_product_collection(self):
        self.connect()
        product_database = self.get_database()
        return product_database['products']

    def search_arrangements(self, arrangements):

        all_arrangements = []
        collection = self.get_product_collection()

        for arrangement in arrangements:
            item = collection.find_one({"id": arrangement})
            item.pop('arrangement')
            item.pop('_id')
            all_arrangements.append(item)

        self.close_connection()
        return all_arrangements

    def get_by_id(self, identifier):

        try:

            collection = self.get_product_collection()

            item = collection.find_one({"id": identifier})
            arrangements = map(int, item['arrangement'].replace('[', "").replace(']', "").split(','))
            item['arrangement'] = self.search_arrangements(arrangements)
            item.pop('_id')

            product = Product(id=item['id'],
                              name=item['name'],
                              price=item['price'],
                              category=item['category'],
                              image=item['image'],
                              arrangement=item['arrangement'],
                              premia_bonus=item['premia_bonus'],
                              price_with_discount=item['price_with_discount'])

            self.close_connection()

            return product
        except Exception:
            return None

    def get_only_arrangement(self, identifier):
        try:

            collection = self.get_product_collection()

            item = collection.find_one({"id": identifier})
            arrangements = map(int, item['arrangement'].replace('[', "").replace(']', "").split(','))
            results = self.search_arrangements(arrangements)

            self.close_connection()

            return results
        except Exception:
            return None

    def all(self):
        try:

            collection = self.get_product_collection()
            products = []

            for item in collection.find({}):
                item.pop('_id')
                item.pop('arrangement')

                product = Product(id=item['id'],
                                  name=item['name'],
                                  price=item['price'],
                                  category=item['category'],
                                  image=item['image'],
                                  premia_bonus=item['premia_bonus'],
                                  price_with_discount=item['price_with_discount'])
                products.append(product)

            self.close_connection()

            return products
        except Exception:
            return None


class OrderDao(Dao):

    def get_order_collection(self):
        self.connect()
        order_database = self.get_database()
        return order_database['orders']

    def search_orders(self):
        try:
            all_orders = []
            collection = self.get_order_collection()

            orders = collection.find({})

            for order in orders:
                order.pop('_id')
                all_orders.append(order)

            self.close_connection()
            return all_orders
        except Exception as e:
            print(e)
            return None


    def post_order(self):
        try:
            orders = self.get_order_collection()
            req = request.get_json(silent=True, force=True)
            req['date'] = datetime.datetime.now()
            orders.insert(req)
            return jsonify(success="Ok")
        except Exception as e:
            print(e)
            return None