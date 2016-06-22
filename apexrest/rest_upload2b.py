#!/usr/bin/Python2
import urllib
import json
import urllib2
import time
import sys
from bmp180 import readBmp180

urlt = 'https://things.ubidots.com/api/v1.6/devices/ServerRoom/Temperature/values?token=owZKtjFwxoYN83wGrw5gMtwSiyQcOz'
urlp = 'https://things.ubidots.com/api/v1.6/devices/ServerRoom/Temperature/values?token=owZKtjFwxoYN83wGrw5gMtwSiyQcOz'

ltemp = None
lpres = None

def getsec():
    t = time.localtime()
    return t.tm_sec

def gettime():
    t = time.localtime()
    dtime = '%s.%s.%s %s:%s:%s ' % (t.tm_mday, t.tm_mon, t.tm_year, 
t.tm_hour, t.tm_min, t.tm_sec)
    return dtime

print('Trivadis Data Uploader for server room 5')
#while 1:
if 1==1:
    ltime = gettime()
    (temperature,pressure) = readBmp180()
    if ltemp != temperature:
        ltemp = temperature
        postdata = {'Temperature': ltemp}
        req = urllib2.Request(urlt)
        req.add_header('Content_Type', 'application/json')
        data=json.dumps(postdata)
        print(ltemp)
        #response = urllib2.urlopen(urlt,postdata)
    #if lpres != pressure:
    #    lpres = pressure
    #    response = urllib2.urlopen(url,getparams(ltime, 'TPRES', pressure)).read()
    #while getsec() > 0:    
    #   time.sleep(1)
