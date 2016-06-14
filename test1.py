import urllib
import urllib2

url = 'http://www.acme.com/users/details'
params = urllib.urlencode({
    'firstName': 'John',
    'lastName' : 'Doe'
})
response = urllib2.urlopen(url, params).read() 
