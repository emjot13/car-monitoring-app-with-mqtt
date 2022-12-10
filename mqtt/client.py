import paho.mqtt.client as mqtt  # import the client1
import time
import database.client as database

TOPICS = ["engine", "tires", "wheel"]


def on_connect(client, userdata, flags, rc):
    for topic in TOPICS:
        client.subscribe(topic)


messages = {
    "engine": [],
    "tires": [],
    "wheel": [],
}

def on_message(client, userdata, message):
    global messages
    if message.topic == "engine":
        msg = str(message.payload.decode("utf-8"))
        messages["engine"].append(msg)
        print("message received ", str(message.payload.decode("utf-8")))
    if message.topic == "tires":
        print("message received ", str(message.payload.decode("utf-8")))
    if message.topic == "wheel":
        print("message received ", str(message.payload.decode("utf-8")))


broker_address = "localhost"
client = mqtt.Client("main_client")
client.on_message = on_message  # attach function to callback
client.on_connect = on_connect  # attach function
client.connect(broker_address)  # connect to broker



def main(plate):
    global messages
    client.loop_start()  # start the loop
    while True:
        database.add_engine_info(plate, messages["engine"])
        time.sleep(10)
# main()
