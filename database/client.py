import pymongo
from database.hash_passwords import hash_password

import time

PORT = 2000
DATABASE_NAME = "main"
COLLECTION_NAME = "cars"


client = pymongo.MongoClient(f"mongodb://localhost:{PORT}/")
database = client[DATABASE_NAME]
cars_collection = database[COLLECTION_NAME]
users_collection = database["users"]

def update_car_info(plates, car_status):
    cars_collection.update_one({"plate": plates}, {"$set": {"car_status": car_status}})


def add_user(name, password):
    password = hash_password(password)
    users_collection.insert_one({"name": name, "password": password})
def find_cars(owner, brand):
    cars = cars_collection.find({"owner": owner})
    cars = [car for car in cars if brand in car["brand"]]
    return cars
def find_cars_by_owner(owner):

    owner_cars = cars_collection.find({"owner": owner})
    return owner_cars


def delete_car(id):
    cars_collection.delete_one({"_id": id})


def find_car_by_plate(plate):
    return cars_collection.find_one({"plate": plate}, projection={"_id": 0})


def update_car(id, plate, owner, brand):
    cars_collection.update_one({"_id": id}, {"$set": {"plate": plate, "owner": owner, "brand": brand}})


def find_car_by_id(id):
    return cars_collection.find_one({"_id": id})


def get_car_info(plates):
    car_info = cars_collection.find_one({"plate": plates}, projection={"car_status": 1, "_id": 0})
    car_info_modified = []
    for key, val in car_info["car_status"].items():
        new_d = {key: val[-2:]}
        car_info_modified.append(new_d)

    return "No data" if car_info is None else car_info_modified
