import paho.mqtt.client as mqtt
import base64
import os
import time
import DHT11 as readtemp
import ReadGPIO as read
topicTemp="drivhus/temp"
topicCmd="AT16/cmd"
topicMaint="drivhus/maint"
topicWet="drivhus/wet"
topicPic="drivhus/pic"
Wetpin=26
Hotpin=19
AT16host="192.168.1.215"

def on_connect(client, userdata, flags, rc):
    print("connected" + str(rc))
    time.sleep(5)
    sub(client)
   
    
def on_message(client, userdata, message):
    time.sleep(1)
    print("Received message "+ str(message.payload) + " on topic "+message.topic)
    if message.topic==topicCmd and message.payload:
        print("post temp")
        postTemp()
        print("post pic")
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

def postTemp():
    client.publish(topicTemp, readtemp.HumTemp(Hotpin))
    client.publish(topicWet, read.Read(Wetpin))


    time.sleep(2)

def sub(client):    
    client.subscribe(topicCmd)
    print("subscribed to :"+topicCmd)
    client.subscribe(topicMaint)
    print("subscribed to :"+topicMaint)
        
client=mqtt.Client("At16client")
client.on_message=on_message
client.on_connect=on_connect
client.connect(AT16host)
time.sleep(5)
client.loop_forever()
