import paho.mqtt.client as mqtt  # import the client1
import time
import random as rd

def tires_status():
    seed = rd.random()
    if seed >= 0.95:
        pressure = rd.randint(100, 140)
        status = "Too high"
    elif seed <= 0.05:
        pressure = rd.randint(0, 60)
        status = "Too low"
    else:
        pressure = rd.randint(60, 100)
        status = "OK"
    return f"{status}-{pressure}"


def main(frequency):
    broker_address = "localhost"
    client = mqtt.Client("tires")
    client.connect(broker_address)
    client.loop_start()
    while True:
        client.publish("tires", tires_status())
        time.sleep(frequency)

