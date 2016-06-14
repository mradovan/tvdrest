import urllib
import urllib2
import time
from bmp180 import readBmp180

url = 'https://apex.oracle.com/pls/apex/kazaliste/postme/testme/'

def getsec():
    t = time.localtime()
    return t.tm_sec

def gettime():
    t = time.localtime()
    dtime = '%s.%s.%s %s:%s:%s ' % (t.tm_mday, t.tm_mon, t.tm_year, 
t.tm_hour, t.tm_min, t.tm_sec)
    return dtime

def getparams(ttyp, tval):
    params = urllib.urlencode({
        'MID': ttyp,
        'VAL': tval
    })
    return params

print('Trivadis Data Uploader for server room 5')
print('Start time: %s' % gettime())
lnow = getsec()
if lnow > 0:
    print('You have to wait %s seconds to start!' % (60 - lnow))
    time.sleep(60-lnow)


print
(temperature,pressure) = readBmp180()
print('Server room data at %s: Temperature: %s C, Pressure: %s hPa' % 
(gettime(), temperature, pressure))
response = urllib2.urlopen(url,getparams('TTEMP', temperature)).read()
response = urllib2.urlopen(url,getparams('TPRES', pressure)).read()
