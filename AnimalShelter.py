# Created by Brandon Kelfstrom 7/22/22

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:55747/?authSource=aac' % ('aacuser', 'aacpassword'))
        self.database = self.client['aac']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            #
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, required):
        if required:
            data = self.database.animals.find(required, {"_id": False})
        else:
            data = self.database.animals.find({}, {"_id": False})

        return data

# Method to implement the U in CRUD
    def update(self, required, data):
        if required:
            find = self.database.animals.update(required, {"_id": False}, {"$set": data}, upsert= False)
        else:
            raise Exception("No file to update")

        return find.json()

# Method to implement the D in CRUD
    def delete(self, required):
        if required:
            data = self.database.animals.delete(required, {"_id": False})
        else:
            raise Exception("No file to delete")

        return 1