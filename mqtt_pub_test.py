#!/usr/bin/env python3
from os import stat
from pydoc import cli
from unittest import result
from datetime import date, datetime
import paho.mqtt.client as mqtt
import time

def mqtt_connect() :
    def on_connect(client, userdata, flags, rc):
        # This will be called once the client connects
        print(f"Connected with result code {rc}")
        # Subscribe here!
    client = mqtt.Client("mqtt-test") # client ID "mqtt-test"
    client.on_connect = on_connect
    client.connect('10.1.45.34', 1883)
    return client

def publish(client):
    msg_count=0
    while msg_count<=400:
        time.sleep(0.002)
        dt=str(datetime.now())
        print(dt)
        result = client.publish("data-raket-topic",dt)
        status=result[0]
        if(status==0):
            print("succes")
            msg_count+=1
        else:
            print("error")

def run():
    client = mqtt_connect()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()