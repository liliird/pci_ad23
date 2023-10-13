import requests
from datetime import datetime

def menu():
    print("1. Conocer los datos meteorológicos")
    print("2. Mostrar ciudades consultadas")
    print("3. Mostrar detalles de una ciudad consultada")
    print("4. Salir")

def getInfo(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"

def printInfoCoordenadas(info):
    print("Longitud:", info.get("lon"))
    print("Latitud:", info.get("lat"))

def printInfoClima(info):
    print("Temperatura en grados Celsius:", info.get("temp"), "°C")
    print("Temperatura en grados Fahrenheit:", info.get("temp") * (9 / 5) + 32, "°F")
    print("Temperatura en grados Kelvin:", info.get("temp") + 273.15, "K")
    print("Humedad:", info.get("humidity"), "%")
    print("Temperatura Mínima:", info.get("temp_min"), "°C")
    print("Temperatura Máxima:", info.get("temp_max"), "°C")
    print("Promedio de temperatura:", (info.get("temp_min") + info.get("temp_max")) / 2, "°C")

def printViento(info):
    print("Viento: ", info.get("speed"))

def main():
    ciudades_consultadas = []  # Lista de ciudades consultadas

    continua = True
    while continua:
        menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            ciudad = input("Introduce la ciudad para conocer su información meteorológica: ")
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&mode=json&units=metric&lang=es&appid=9fc4e2b08423fd7dbcf8a27d0e755035"
            response = getInfo(url)
            if response != "Error":
                print("Ciudad:", response.get("name"))
                printInfoCoordenadas(response.get("coord"))
                printInfoClima(response.get("main"))
                printViento(response.get("wind"))
                # Información de la ciudad consultada en la lista como un diccionario
                ciudad_info = {
                    "name": response.get("name"),
                    "coord": response.get("coord"),
                    "main": response.get("main"),
                    "wind": response.get("wind")
                }
                ciudades_consultadas.append(ciudad_info)
            else:
                print(response)
        elif opcion == 2:
            print("Ciudades consultadas:")
            for i, ciudad in enumerate(ciudades_consultadas):
                print(f"{i + 1}. {ciudad['name']}")
        elif opcion == 3:
            indice = int(input("Introduce el número de la ciudad para ver sus detalles: ")) - 1
            if 0 <= indice < len(ciudades_consultadas):
                cd_selec= ciudades_consultadas[indice]
                print("Detalles de la ciudad seleccionada:")
                print("Ciudad:", cd_selec["name"])
                printInfoCoordenadas(cd_selec["coord"])
                printInfoClima(cd_selec["main"])
                printViento(cd_selec["wind"])
            else:
                print("Índice de ciudad no válido.")
        elif opcion == 4:
            print("Adiós")
            continua = False

if __name__ == "__main__":
    main()
