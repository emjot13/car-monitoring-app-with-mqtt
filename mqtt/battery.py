import paho.mqtt.client as mqtt
import time
import random as rd

def battery_status():
    if rd.random() >= 0.8:
        battery_percentage = rd.randint(2, 20)
        status = "Too low"
    else:
        battery_percentage = rd.randint(21, 100)
        status = "OK"
    return f"{status}-{battery_percentage}"


def main(frequency):
    broker_address = "localhost"
    client = mqtt.Client("battery")
    client.connect(broker_address)
    client.loop_start()
    while True:
        client.publish("battery", battery_status())
        time.sleep(frequency)

