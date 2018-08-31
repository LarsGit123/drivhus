import paho.mqtt.client as mqtt
import InspectPic as inspect
import time
import MQTTpub as pub

topicPic="Kvikne/pic"
AT16host="192.168.1.216"
SubClient="SubPicClient"
PictureSavePath='/home/pi/webcam/KvikneCam.jpg'

def on_connect(client, userdata, flags, rc):
    print("connected" + str(rc))
    time.sleep(5)
    sub(client)
   
    
def on_message(client, userdata, message):    
    print("Received message on topic "+message.topic)
    if message.topic==topicPic :
        print("Got Picture")
        SavePic(message.payload, PictureSavePath)
        PostAnalysis(PictureSavePath)
    elif message.topic==topicMaint and message.payload:
        client.disconnect()
        time.sleep(5)
        client.connect(AT16host)

def SavePic(byteString, path):
    file=open(path, 'wb')
    file.write(bytearray(byteString))
    file.close()
    print("Saved picture as "+PictureSavePath)

def PostAnalysis(picturepath):
    img=inspect.GetImage(picturepath)
    MaxXY=inspect.GetMaxXY(img)
    RelAvgIntensity=round(inspect.GetAvgIntensity(img,MaxXY)/2.5,1)
    pub.MqttPub("SolScore: "+str(RelAvgIntensity), "Kvikne/sol",AT16host)

def sub(client):    
    client.subscribe(topicPic)
    print("subscribed to :"+topicPic)
    
        
client=mqtt.Client(SubClient)
client.on_message=on_message
client.on_connect=on_connect
client.connect(AT16host)
time.sleep(5)
client.loop_forever()
