from bson.objectid import ObjectId
from django.shortcuts import render, redirect

import mqtt.client
from database.client import cars_collection
from database.client import users_collection
from mqtt import client, sensor_launcher
import database.client as database
import threading
from database.hash_passwords import hash_password


def login(request):
    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("pass")
        user = users_collection.find_one({"login": login})
        if user is not None:
            user_hashed_password = user["password"]
            if user_hashed_password == hash_password(password):
                return render(request, "main_page.html")

    return render(request, "login.html")

def start_page(request):
    return render(request, "start_page.html")

def register(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("pass")
        password1 = request.POST.get("pass1")
        if password1 == password:
            hashed_password = hash_password(password)
            users_collection.insert_one({"login": login, "password": hashed_password})
            return render(request, "login.html")

    return render(request, "register.html")


def start(request):
    return render(request, "main_page.html")


def see_my_cars(request):
    if request.method == "POST" and "owner" in request.POST:
        owner = request.POST.get("owner")
        brand = request.POST.get("brand")
        if brand:
            cars = database.find_cars(owner, brand)
        else:
            cars = database.find_cars_by_owner(owner)

        cars = list(cars)
        for car in cars:
            car["id"] = car["_id"]
        return render(request, "see_my_cars.html", {"cars": cars})

    return render(request, "see_my_cars.html")


def delete_car(request):
    id = request.POST.get("id")
    id = ObjectId(id)
    database.delete_car(id)
    return render(request, "see_my_cars.html")


def add_car_form(request):
    return render(request, "add_car.html")


def update_car(request):
    id = request.POST.get("id")
    id = ObjectId(id)
    plate = request.POST.get("plate")
    owner = request.POST.get("owner")
    brand = request.POST.get("brand")
    database.update_car(id, plate, owner, brand)
    return render(request, "see_my_cars.html")


def update_car_form(request):
    id = request.POST.get("id")
    mongo_id = ObjectId(id)
    car = database.find_car_by_id(mongo_id)
    car["id"] = id
    return render(request, "update_car.html", {"car": car})


def add_car(request):
    if request.method == "POST":
        plate = request.POST.get("plate")
        car_owner = request.POST.get("car_owner")
        brand = request.POST.get("brand")
        car = {"plate": plate, "owner": car_owner, "brand": brand, "car_status": {}}
        cars_collection.insert_one(car)
    return redirect("http://127.0.0.1:8000/start")


def see_car_status(plate):
    return database.get_car_info(plate)


def check_car(request):
    if request.method == "POST":
        plate = request.POST.get("plate")
        mqtt_client = threading.Thread(target=mqtt.client.main, args=(plate,))
        mqtt_sensors = threading.Thread(target=mqtt.sensor_launcher.launch)
        mqtt_client.start()
        mqtt_sensors.start()
        car_status = see_car_status(plate)
        return render(request, "check_car_status.html", {"car_status": car_status})

    return render(request, "check_car_status.html")
