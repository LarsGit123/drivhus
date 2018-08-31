import paho.mqtt.client as mqtt
import base64
import os
import time
topicPic="Drivhus/pic"
topicCmd="Drivhus/cmd"
topicMaint="Drivhis/maint"
AT16host="178.164.99.145"

def on_connect(client, userdata, flags, rc):
    print("connected" + str(rc))
    time.sleep(5)
    sub(client)
   
    
def on_message(client, userdata, message):
    time.sleep(1)
    print("Received message "+ str(message.payload) + " on topic "+message.topic)
    if message.topic==topicCmd and message.payload:
        print("post picture")
        postPic()
    elif message.topic==topicMaint and message.payload:
        client.disconnect()
        time.sleep(5)
        client.connect(AT16host)

def postPic():
    with open("/home/pi/webcam/snapshot.jpg", "rb") as imageFile:
            bInString= imageFile.read()
            byteArr=bytes(bInString)
            client.publish(topicPic, byteArr, 0)            
            print("publish pic on topic "+topicPic)
            time.sleep(2)

def sub(client):    
    client.subscribe(topicCmd)
    print("subscribed to :"+topicCmd)
    client.subscribe(topicMaint)
    print("subscribed to :"+topicMaint)
        
client=mqtt.Client("KvikneClient")
client.on_message=on_message
client.on_connect=on_connect
client.connect(AT16host)
time.sleep(5)
