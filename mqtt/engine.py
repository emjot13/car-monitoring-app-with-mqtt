import paho.mqtt.client as mqtt  # import the client1
import time
import random as rd

def engine_status():
    seed = rd.random()
    if seed >= 0.9:
        temperature = rd.randint(96, 140)
        status = "Too hot"
    elif seed <= 0.1:
        temperature = rd.randint(0, 59)
        status = "Too low"
    else:
        temperature = rd.randint(60, 95)
        status = "OK"
    return f"{status}-{temperature}"


def main(frequency):
    broker_address = "localhost"
    client = mqtt.Client("engine")
    client.connect(broker_address)
    client.loop_start()
    while True:
        client.publish("engine", engine_status())
        time.sleep(frequency)

