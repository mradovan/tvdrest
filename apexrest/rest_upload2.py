import urllib
import urllib2
import time
from bmp180 import readBmp180

url = 'https://apexea.oracle.com/pls/apex/mradovan/postdata/measvals/'

def getsec():
    t = time.localtime()
    return t.tm_sec

def gettime():
    t = time.localtime()
    dtime = '%s.%s.%s %s:%s:%s ' % (t.tm_mday, t.tm_mon, t.tm_year, 
t.tm_hour, t.tm_min, t.tm_sec)
    return dtime

def getparams(ptime, ttyp, tval):
    params = urllib.urlencode({
        'DTIME' : ptime,
        'MID'   : ttyp,
        'VAL'   : tval
    })
    return params

ltime = gettime()
print('Trivadis Data Uploader for server room 5')
print('Start time: %s' % ltime)
lnow = getsec()
if lnow > 0:
    print('You have to wait %s seconds to start!' % (60 - lnow))
    time.sleep(60-lnow)


print
(temperature,pressure) = readBmp180()
print('Server room data at %s: Temperature: %s C, Pressure: %s hPa' % 
(ltime, temperature, pressure))
response = urllib2.urlopen(url,getparams(ltime, 'TTEMP', temperature)).read()
response = urllib2.urlopen(url,getparams(ltime, 'TPRES', pressure)).read()
