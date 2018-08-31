# -*- coding: utf-8 -*-
import MQTTpub
import time
import ReadGPIO as read
import DHT11 as readtemp

IsWetPin=26
TempPin=19
sleeptime=120
HumCounterTarget=6
HumCounter=0



while True:
    if HumCounter==HumCounterTarget:
        HumCounter=0
        IsWet= read.Read(IsWetPin)
        IsHot= readtemp.HumTemp(TempPin)
        print(IsWet)
        print(IsHot)
        MQTTpub.MqttPub(str(IsHot), "drivhus/temp")
        if IsWet==False:
            MQTTpub.MqttPub("MåVanne", "drivhus/hum")            
        else:
            MQTTpub.MqttPub("Vann ok", "drivhus/hum")                  
        print(IsWet)
    print(str(HumCounter)+ "/"+str(HumCounterTarget))
    HumCounter=HumCounter+1
    time.sleep(sleeptime)
    
