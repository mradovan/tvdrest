import urllib
import urllib2

url = 'https://apex.oracle.com/pls/apex/kazaliste/postme/testme/'
params = urllib.urlencode({
    'MID': 'TTEMP',
    'VAL' : 19.4
})
response = urllib2.urlopen(url, params).read() 
