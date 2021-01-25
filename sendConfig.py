#!/usr/bin/env python3
import sys
import json
import time
import string
import serial
from time import sleep


import os
import re

try:
        file = open('configData.json','r')
        configData =  json.load(file)
        d1 = str(configData['light'])
        d1_len = len(d1)
        temp_s =''
        
        for x in range(4-d1_len):
                temp_s+='0'
        temp_s+=d1
        d1 = temp_s
        
        d2 = str(configData['hum'])
        d2_len = len(d2)
        temp_s =''
        
        for x in range(3-d2_len):
                temp_s+='0'
        temp_s +=d2
        d2=temp_s
                
        d3 = str(configData['temp'])
        d3_len = len(d3)
        temp_s =''
        
        for x in range(2-d2_len):
                temp_s+='0'
        temp_s +=d3
        d3=temp_s
        
        sendString = d1+d2+d3
        
        ser = serial.Serial("/dev/ttyACM0", 9600)    #Open port with baud rate
        ser.write(sendString.encode())
        file.close()
except KeyboardInterrupt:
    pass
