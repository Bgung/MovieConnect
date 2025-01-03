import os

from pymongo import MongoClient
from urllib.parse import quote_plus
from bson.objectid import ObjectId

class Base:
    def __init__(self, database, collection):
        uri = "mongodb://%s:%s@%s:%s" % (
            quote_plus(os.environ['MONGO_USER']),
            quote_plus(os.environ['MONGO_PASSWORD']),
            os.environ['MONGO_HOST'],
            os.environ['MONGO_PORT']
        )
        print(uri)
        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def find_all(self):
        return self.collection.find()

    def find(self, query):
        return self.collection.find(query)
    
    def find_by_id(self, id):
        return self.collection.find_one({'_id': ObjectId(id)})
    
    def insert(self, data):
        return self.collection.insert_one(data)
    
    def update(self, query, data):
        if query.get('_id'):
            query['_id'] = ObjectId(query['_id'])
        return self.collection.update_one(query, data).acknowledged
    
    def delete(self, query):
        return self.collection.delete_one(query)
    
    def count(self, query):
        return self.collection.count_documents(query)
