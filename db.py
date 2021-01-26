import requests
from pymongo import MongoClient


class MongoDB(object):
    def __init__(self, host='localhost', port=27017, database_name=None, collection_name=None, index=None):
        try:
            self._connection = MongoClient(host=host, port=port, maxPoolSize=200)
        except Exception as error:
            raise Exception(error)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._connection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]
        if index:
            self._collection.create_index(index, unique=True)

    def insert(self, post):
        # add/append/new single record
        post_id = self._collection.insert_one(post)
        return post_id

    def insert_many(self, data):

        data_id = self._collection.insert_many(data)
        
