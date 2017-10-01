import os
from pymongo import MongoClient

class Dao:
    def connect(self):
        # self.client = MongoClient('localhost', 27017)
        self.client = MongoClient(os.environ['MONGO'])

    def close_connection(self):
        self.client.close()
