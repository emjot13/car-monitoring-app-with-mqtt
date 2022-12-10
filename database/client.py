import pymongo

PORT = 2000
DATABASE_NAME = "main"
COLLECTION_NAME = "cars"


client = pymongo.MongoClient(f"mongodb://localhost:{PORT}/")
database = client[DATABASE_NAME]
cars_collection = database[COLLECTION_NAME]


def add_engine_info(plates, engine_status):
    cars_collection.update_one({"plate": plates}, {"$set" : {"engine_status": engine_status}})



