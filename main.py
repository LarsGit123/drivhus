# -*- coding: utf-8 -*-
import MQTTpub
import time
import ReadGPIO as read

sleeptime=1
HumCounterTarget=6
HumCounter=0

while True:
    if HumCounter==HumCounterTarget:
        HumCounter=0
        IsWet= read.Read(26)
        print(IsWet)
        if IsWet==False:
            MQTTpub.MqttPub("MåVanne", "drivhus/hum")            
        else:
            MQTTpub.MqttPub("Vann ok", "drivhus/hum")                  
        print(IsWet)
    print(str(HumCounter)+ "/"+str(HumCounterTarget))
    HumCounter=HumCounter+1
    time.sleep(sleeptime)
    
