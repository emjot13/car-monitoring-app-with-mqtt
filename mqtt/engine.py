import paho.mqtt.client as mqtt  # import the client1
import time


def main():
    broker_address = "localhost"
    # broker_address="iot.eclipse.org"
    client = mqtt.Client("engine")  # create new instance# attach function
    client.connect(broker_address)  # connect to broker
    client.loop_start()  # start the loop
    while True:
        client.publish("engine", "OK")
        print("published")
        time.sleep(2)

# main()