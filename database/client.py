import pymongo
import time

PORT = 2000
DATABASE_NAME = "main"
COLLECTION_NAME = "cars"


client = pymongo.MongoClient(f"mongodb://localhost:{PORT}/")
database = client[DATABASE_NAME]
cars_collection = database[COLLECTION_NAME]


def update_car_info(plates, car_status):
    cars_collection.update_one({"plate": plates}, {"$set": {"car_status": car_status}})


def get_car_info(plates):
    car_info = cars_collection.find_one({"plate": plates}, projection={"car_status": 1, "_id": 0})
    print(car_info)
    car_info_modified = []
    for key, val in car_info["car_status"].items():
        new_d = {key: val[-2:]}
        car_info_modified.append(new_d)

    # print(car_info.values())
    # print([{key: value[:2]} for item in car_info.values()])
    return "No data" if car_info is None else car_info_modified
