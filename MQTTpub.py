import paho.mqtt.client as mqtt

def MqttPub(msg, topic, ip, clientName="at16"):
    client= mqtt.Client(clientName)
    client.connect(ip)
    print("connected")    
    client.publish(topic, msg)
    print("publish: " + msg + " to " + topic)
    client.disconnect()
    print("disconnected")
