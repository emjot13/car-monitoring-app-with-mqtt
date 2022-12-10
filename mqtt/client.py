import paho.mqtt.client as mqtt  # import the client1
import time
import database.client as database

TOPICS = ["engine", "tires", "brakes_fluid", "fuel", "oil", "battery"]
UNITS = ["temperature", "pressure", "percentage", "percentage", "percentage", "percentage"]
messages = {topic: [] for topic in TOPICS}


def on_connect(client, userdata, flags, rc):
    for topic in TOPICS:
        client.subscribe(topic)


def on_message(client, userdata, message):
    global messages
    status, value = str(message.payload.decode("utf-8")).split("-", 1)
    for topic, unit in zip(TOPICS, UNITS):
        if message.topic == topic:
            messages[topic].append({status: {unit: value}})
            break


broker_address = "localhost"
client = mqtt.Client("main_client")
client.on_message = on_message
client.on_connect = on_connect
client.connect(broker_address)


def main(plate):
    global messages
    client.loop_start()
    while True:
        database.update_car_info(plate, messages)
        time.sleep(15)

