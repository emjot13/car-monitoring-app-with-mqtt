import paho.mqtt.client as mqtt
import time
import random as rd

def brakes_fluid_status():
    if rd.random() >= 0.8:
        brakes_fluid_percentage = rd.randint(2, 20)
        status = "Too low"
    else:
        brakes_fluid_percentage = rd.randint(21, 100)
        status = "OK"
    return f"{status}-{brakes_fluid_percentage}"


def main(frequency):
    broker_address = "localhost"
    client = mqtt.Client("brakes_fluid")
    client.connect(broker_address)
    client.loop_start()
    while True:
        client.publish("brakes_fluid", brakes_fluid_status())
        time.sleep(frequency)

