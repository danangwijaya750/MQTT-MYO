from datetime import datetime
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe("data-raket-topic")

def on_message(client, userdata, msg):
    with open('_test_mqtt.csv','a') as f :
        f.write(str(msg.payload.decode("utf-8")) + ";" + str(datetime.now()) + "\n")

client = mqtt.Client("mqtt_tester")
client.on_connect = on_connect
client.on_message = on_message
#client.connect("127.0.0.1",1883)
client.connect("broker.hivemq.com",1883)
client.loop_forever()
