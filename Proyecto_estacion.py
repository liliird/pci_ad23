import requests
from datetime import datetime
import datetime

def getInfo(url):
    response=requests.get(url)
    if(response.status_code==200):
        return response.json()
    else:
        return "Error"

def printInfoCoordenadas(info):
    print("Longitud:",info.get("lon"))
    print("Latitud:",info.get("lat"))

def printInfoClima(info):
    print("Temperatura en grados Celsius:",info.get("temp"), "°C")
    print("Temperatura en grados Fahrenheit:",info.get("temp")*(9/5)+32, "°F")
    print("Temperatura en grados Kelvin:",info.get("temp")+273.15, "K")
    print("Humedad:",info.get("humidity")) 
    print("Temperatura Mínima:",info.get("temp_min"))
    print("Temperatura Máxima:",info.get("temp_max"))
    print("Promedio de temperatura:",(info.get("temp_min")+info.get("temp_max"))/2)
    
def printViento(info):
    print("Viento: ",info.get("speed"))
    
ciudad=input("Introduce la ciudad para conocer su información meteorológica: ")
url="http://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&mode=json&units=metric&lang=es&appid=9fc4e2b08423fd7dbcf8a27d0e755035"
response=getInfo(url)
if (response!="Error"):
    print("Ciudad:",response.get("name"))
    printInfoCoordenadas(response.get("coord"))
    printInfoClima(response.get("main"))
    printViento(response.get("wind"))
else:
    print(response)
