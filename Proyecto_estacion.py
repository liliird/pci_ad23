import requests
from datetime import datetime
from statistics import mean, median, mode

def menu():
    print("\n1. Conocer los datos meteorológicos")
    print("2. Mostrar ciudades consultadas")
    print("3. Mostrar detalles de una ciudad consultada")
    print("4. Salir")
    print("--------------------------------------------------------------------------------")

def get_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"

def print_info_coordenadas(info):
    print("Longitud:", info.get("lon"))
    print("Latitud:", info.get("lat"))

def print_info_clima(info):
    temp = info.get("temp")
    temp_min = info.get("temp_min")
    temp_max = info.get("temp_max")
    #Uso de operadores aritméticos para conocer la temperatura en diferentes unidades de medida
    print("Temperatura en grados Celsius:", temp, "°C")
    print("Temperatura en grados Fahrenheit:", temp * (9 / 5) + 32, "°F")
    print("Temperatura en grados Kelvin:", temp + 273.15, "K")
    print("Humedad:", info.get("humidity"), "%")
    print("Temperatura Mínima:", temp_min, "°C")
    print("Temperatura Máxima:", temp_max, "°C")
    
    # Calculamos la media, mediana y moda de las temperaturas con ayuda de la librería statistics 
    temperaturas = [temp, temp_min, temp_max]
    
    print("Media de temperatura:", mean(temperaturas), "°C")
    print("Mediana de temperatura:", median(temperaturas), "°C")
    
    try:
        print("Moda de temperatura:", mode(temperaturas), "°C")
    except:
        print("No hay moda para las temperaturas")

def print_viento(info):
    print("Viento: ", info.get("speed"))

def main():
    ciudades_consultadas = []  # Lista de ciudades consultadas

    continua = True
    while continua:
        menu()
        opcion = int(input("Introduce una opción: "))
        print("--------------------------------------------------------------------------------")
        if opcion == 1:
            ciudad = input("Introduce la ciudad para conocer su información meteorológica: ")
            #URL de la API obtenida de OpenWeatherMap
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&mode=json&units=metric&lang=es&appid=9fc4e2b08423fd7dbcf8a27d0e755035"
            response = get_info(url)
            if response != "Error":
                print("Ciudad:", response.get("name"))
                print_info_coordenadas(response.get("coord"))
                print_info_clima(response.get("main"))
                print_viento(response.get("wind"))
                # Información de la ciudad consultada en la lista como un diccionario
                ciudad_info = {
                    "name": response.get("name"),
                    "coord": response.get("coord"),
                    "main": response.get("main"),
                    "wind": response.get("wind"),
                    "historial": []  # Lista anidada para almacenar el historial de consultas
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
                print_info_coordenadas(cd_selec["coord"])
                print_info_clima(cd_selec["main"])
                print_viento(cd_selec["wind"])
            else:
                print("Índice de ciudad no válido.")
        elif opcion == 4:
            print("Adiós")
            continua = False

if __name__ == "__main__":
    main()
