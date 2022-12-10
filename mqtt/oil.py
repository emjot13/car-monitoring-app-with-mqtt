import paho.mqtt.client as mqtt
import time
import random as rd

def oil_status():
    if rd.random() >= 0.8:
        oil_percentage = rd.randint(2, 20)
        status = "Too low"
    else:
        oil_percentage = rd.randint(21, 100)
        status = "OK"
    return f"{status}-{oil_percentage}"


def main(frequency):
    broker_address = "localhost"
    client = mqtt.Client("fuel")
    client.connect(broker_address)
    client.loop_start()
    while True:
        client.publish("oil", oil_status())
        time.sleep(frequency)

