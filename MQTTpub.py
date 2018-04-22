import paho.mqtt.client as mqtt

def MqttPub(msg, topic):
    client= mqtt.Client("at16")
    client.connect("192.168.1.237")
    print("connected")    
    client.publish(topic, msg)
    print("publish: " + msg + " to " + topic)
    client.disconnect()
    print("disconnected")
