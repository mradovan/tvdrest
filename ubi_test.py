#Trivadis (C) 2016 
#RMI 09.06.2016

from ubidots import ApiClient
import math
import time

# Create an ApiClient object

api = ApiClient(token='Bx2jZVG7VAlsoxsLjnbJewKcj8qfiZ')

# Get a Ubidots Variable

variable = api.get_variable('575958367625426ead141395')

# Place for code to capture data from the sensor

cnt = 0
while (cnt < 10):
    # value to my variable in Ubidots
    response = variable.save_value({"value": 20*math.sin(cnt)})
    print (response)
    cnt += 1
    time.sleep(10)

