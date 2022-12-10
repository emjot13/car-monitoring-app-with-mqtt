import paho.mqtt.client as mqtt
import time
import random as rd

def fuel_status():
    if rd.random() >= 0.8:
        fuel_percentage = rd.randint(2, 20)
        status = "Too low"
    else:
        fuel_percentage = rd.randint(21, 100)
        status = "OK"
    return f"{status}-{fuel_percentage}"


def main(frequency):
    broker_address = "localhost"
    client = mqtt.Client("fuel")
    client.connect(broker_address)
    client.loop_start()
    while True:
        client.publish("fuel", fuel_status())
        time.sleep(frequency)

