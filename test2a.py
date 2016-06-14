import urllib
import urllib2
import time
from bmp180 import readBmp180

url = 'https://apex.oracle.com/pls/apex/kazaliste/postme/testme/'

def getparams():
    params = urllib.urlencode({
        'MID': 'TTEMP',
        'VAL' : 16.2
    })
    return params

response = urllib2.urlopen(url,getparams()).read() 
