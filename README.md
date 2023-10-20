# pci_ad23

Contexto:
Una estación meteorológica está diseñada para medir y registrar elementos relacionados con condiciones climáticas de algún lugar, como la temperatura, la humedad, la presión atmosférica, la precipitación, la velocidad y dirección del viento, entre otras características del entorno atmosférico.
Los datos recabados de una estación meteorológica son valiosos para la elaboración de pronósticos meteorológicos a largo y corto plazo.
En general, una estación meteorológica es una herramienta bastante importante y escencial para la recopilación de datos climáticos y meteorológicos, lo que contribuye a la comprensión y la predicción del clima en una región determinada.

Un proyecto como una estación meteorológica brinda una oportunidad concreta para aplicar conceptos de programación, traduciendo el conocimiento teórico en una solución real y funcional, permitiendo desarrollar habilidades en la manipulación de datos, diseño de interfaz de usuario, gestión lógica del programa, etc. La programación de este proyecto, implica la solución de desafíos técnicos, desde la integración de API para obtener los datos climáticos hasta la visualizaión de la información.
En resumen, codificar una estación meteorológica como un proyecto ofrece una manera efectiva de combinar teoría y práctica, para el desarrollo de habilidades en la programación.

Este programa es un buscador de condiciones climáticas en un lugar determinado por el usuario. Los datos serán recabados desde una API y mostrados al usuario.



El algoritmo para el funcionamiento del programa se puede describir de la siguiente manera:

1. El programa comienza con la ejecución de la función main().
2. Se inicializa una lista vacía llamada ciudades_consultadas para almacenar información sobre las ciudades consultadas.
3. Se inicia un bucle while que permite al usuario interactuar con el programa a través de un menú.
4. El menú se muestra utilizando la función menu(), y el usuario selecciona una opción introduciendo un número.
5. Si el usuario elige la opción 1, se le solicita que ingrese el nombre de una ciudad.
6. El programa construye una URL para obtener datos meteorológicos de la ciudad proporcionada utilizando la API de OpenWeatherMap. Luego, se llama a la función getInfo(url) para obtener la respuesta de la API.
7. Si la respuesta es exitosa y no es un error, se muestra información sobre la ciudad, incluyendo la temperatura en grados Celsius, Fahrenheit y Kelvin, la humedad, la temperatura mínima y máxima, y se calcula la media, la mediana y la moda de las temperaturas.
8. La información de la ciudad consultada se almacena en un diccionario y se agrega a la lista ciudades_consultadas. Además, se crea una lista anidada vacía llamada "historial" para almacenar el historial de consultas de esa ciudad.
9. Si el usuario elige la opción 2, se muestra una lista de las ciudades consultadas hasta ese momento.
10. Si el usuario elige la opción 3, se le pide que ingrese el número de la ciudad de la lista que desea ver en detalle.
11. Si el índice es válido, se muestra información detallada de la ciudad, incluyendo coordenadas, datos climáticos y velocidad del viento.
12. Si el usuario elige la opción 4, el programa muestra "Adiós" y sale del bucle, finalizando la ejecución.
13. El programa se ejecuta hasta que el usuario elige salir, momento en el cual termina.
    
El programa permite al usuario conocer datos meteorológicos de ciudades, almacenar un historial de consultas y calcular estadísticas de temperatura. También maneja errores si la ciudad ingresada no se encuentra o si la API no responde correctamente.

DATO: Un dato importante a considerar, es que para la ejecución del código es necesario instalar previamente las librerías requests, datetime y statistics. Podemos realizar esto desde el cmd de nuestro equipo con el comando: pip install <nombre_de_la_libreria>
