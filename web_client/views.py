from django.shortcuts import render, redirect

import mqtt.client
import web_client.views
from database.client import cars_collection
from mqtt import client, engine, tires, wheel

import threading


def start(request):
    return render(request, "start_page.html")



def add_car_form(request):
    # mqtt.client.main()
    # mqtt.engine.main()

    return render(request, "add_car.html")


def add_car(request):
    if request.method == "POST":
        plate = request.POST.get("plate")
        car_owner = request.POST.get("car_owner")
        car = {"plate": plate, "owner": car_owner, "engine_status": [], "tires_status": [], "wheel_status": []}
        cars_collection.insert_one(car)
    return redirect("http://127.0.0.1:8000/")


def check_car_form(request):
    return render(request, "check_car_status.html")


def check_car(request):
    if request.method == "POST":
        plate = request.POST.get("plate")
        mqtt_client = threading.Thread(target=mqtt.client.main, args=(plate,))
        mqtt_engine = threading.Thread(target=mqtt.engine.main)
        mqtt_client.start()
        mqtt_engine.start()
    return render(request, "check_car_status.html")
