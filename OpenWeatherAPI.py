import json
import urllib.request

#Kelvin to Celsius conversion
def K2C(K):
    C = K - 273.15
    return C

res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+"Taipei"+"&appid=10121bcf75859cffa376f7794823b678").read()
json_data = json.loads(res)
print (json_data)
Kelvin = json_data['main']['temp']
print (K2C(Kelvin))


