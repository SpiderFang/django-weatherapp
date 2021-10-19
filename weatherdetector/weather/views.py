from django.shortcuts import render, redirect
import json
import urllib.request

"""
Custom functions
"""
#Kelvin to Celsius conversion
def K2C(K):
    C = K - 273.15
    return C

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if (city != "") and (city.isspace() != True): #判斷非空字串和空白
            res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=10121bcf75859cffa376f7794823b678").read()
            json_data = json.loads(res)
            Kelvin = json_data['main']['temp']
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon'])+", "+str(json_data['coord']['lat']),
                "temp": str(K2C(Kelvin))+"C",
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity'])+"%"
            }
        else:
            city = ''
            data = {}
            return redirect('/')
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {"city": city, "data": data})
