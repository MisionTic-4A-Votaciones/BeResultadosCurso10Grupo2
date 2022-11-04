import json

import certifi
import pymongo
from typing import Generic, TypeVar, get_args

from bson import ObjectId

T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __init__(self):
        # connect to database
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tlsCAFILe=ca
        )
        self.data_base = client[data_config.get("db-name")]
        # get generic class name
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self):
        with open("config.json", 'r') as config:
            data = json.load(config)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find({}):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        # si el _id no esta, document = None
        document = current_collection.find_one({'_id': _id})
        document = self.get_values_db_ref(document)
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            document = {}
        return document

    def save(self, item: T) -> T:
        current_collection = self.data_base[self.collection]
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            # update
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item = item.__dict__
            updated_item = {"$set": item}
            current_collection.update_one({'_id': _id}, updated_item)
        else:
            # insert
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        return self.find_by_id(id_)

    def update(self, id_: str, item: T) -> dict:
        pass

    def delete(self, id_: str) -> dict:
        pass

    def query(self, query: dict) -> list:
        pass

    def query_aggregation(self, query: dict) -> list:
        pass

    def get_values_db_ref(self):
        pass

    def get_values_db_ref_from_list(self):
        pass

    def transform_object_ids(self):
        pass

    def transform_refs(self):
        pass

    def format_list(self):
        pass

    def object_to_db_ref(self):
        pass
    

    