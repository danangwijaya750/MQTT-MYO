from datetime import datetime
from pydoc import cli
import paho.mqtt.client as mqtt
import PySimpleGUI as sg

layout =[[sg.Text("Handler MQTT")],[sg.Button("Start")],[sg.Button("Stop")]]
window=sg.Window("Handler MQTT",layout)

imu_data=[]
wrting=False
def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe("data_raket_topic")

def on_message(client, userdata, msg):
    global imu_data
    if wrting == False :
        imu_data.append(str(msg.payload.decode("utf-8")) + ";" + str(datetime.now()))
    # with open('_test_mqtt.csv','a') as f :
    #     f.write(str(msg.payload.decode("utf-8")) + ";" + str(datetime.now()) + "\n")

def writingData():
    global wrting
    global imu_data
    print(len(imu_data))
    wrting=False
    for i in imu_data :
        with open('_test_mqtt.csv','a') as f :
            f.write(i + "\n")

client = mqtt.Client("mqtt_tester")
client.on_connect = on_connect
client.on_message = on_message
#client.connect("127.0.0.1",1883)


while True:
    event, values = window.read()
    if(event=="Start") :
        print("start")
        client.connect("broker.hivemq.com",1883)
        client.loop_start()
    elif(event=="Stop") :
        print("stop")
        writingData()
        client.loop_stop()
    elif(event==sg.WIN_CLOSED):
        break

window.close
