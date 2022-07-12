from datetime import datetime
import paho.mqtt.client as mqtt

msg_count = 0
def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe("data-raket-topic")

def on_message(client, userdata, msg):
    dt =str(datetime.now())
    global msg_count
    print(dt,msg_count,msg.payload)
    msg_count+=1

client = mqtt.Client("mqtt_tester")
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1",1883)
client.loop_forever()
