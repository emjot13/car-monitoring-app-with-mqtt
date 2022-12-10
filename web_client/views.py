from django.shortcuts import render, redirect

import mqtt.client
from database.client import cars_collection
from mqtt import client, sensor_launcher
import database.client as database
import threading


def start(request):
    return render(request, "start_page.html")



def add_car_form(request):
    # mqtt.client.main()
    # mqtt.engine.main()

    return render(request, "add_car.html")


def add_car(request):
    if request.method == "POST":
        print("Adding")
        plate = request.POST.get("plate")
        car_owner = request.POST.get("car_owner")
        car = {"plate": plate, "owner": car_owner, "car_status": {}}
        cars_collection.insert_one(car)
    return redirect("http://127.0.0.1:8000/")


# def check_car_form(request):
#     return render(request, "check_car_status.html")

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
