#!/usr/bin/env python3
import sys
import json
import time
import string
import serial
from time import sleep


import os
import re

licznik1 = 0
licznik2 =0
licznik3 =0

try:
    while True:
        seconds = time.time()
        ser = serial.Serial("/dev/ttyACM0", 9600)    #Open port with baud rate
        received_data = ser.read()              #read serial port
        sleep(0.03)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        decoded_data = received_data.decode("utf-8")
        temp = re.findall(r'\d+', decoded_data)
        light = int(temp[0])
        humidity = int(temp[1])
        temperature = float(temp[2]+"."+temp[3])
        res = list(map(int, temp))
        print (light, humidity, temperature)                   #print received data
     #____________________________#

        data = [{'Light':light, 'Unit':'Lux'},
        {'Temperature':temperature, 'Unit':'Celsius Degrees'},
        {'Humidity':humidity, 'Unit':'%'}]
        try:
            with open('alldata.json','w') as outfile:
                json.dump(data,outfile)
        finally:
            outfile.close()
        time.sleep(0.1)
        wholedata = [{'Light':light, 'Unit':'Lux'},
        {'Temperature':temperature, 'Unit':'Celsius Degrees'},
        {'Humidity':humidity, 'Unit':'%'}]
        try:
            with open('wholedata.json','a') as wholefile:
                wholefile.write("\n")
                json.dump(wholedata,wholefile)
                wholefile.write(time.ctime(seconds))
        finally:
            wholefile.close()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass