# pci_ad23

Contexto:
Una estación meteorológica está diseñada para medir y registrar elementos relacionados con condiciones climáticas de algún lugar, como la temperatura, la humedad, la presión atmosférica, la precipitación, la velocidad y dirección del viento, entre otras características del entorno atmosférico.
Los datos recabados de una estación meteorológica son valiosos para la elaboración de pronósticos meteorológicos a largo y corto plazo.
En general, una estación meteorológica es una herramienta bastante importante y escencial para la recopilación de datos climáticos y meteorológicos, lo que contribuye a la comprensión y la predicción del clima en una región determinada.

Un proyecto como una estación meteorológica brinda una oportunidad concreta para aplicar conceptos de programación, traduciendo el conocimiento teórico en una solución real y funcional, permitiendo desarrollar habilidades en la manipulación de datos, diseño de interfaz de usuario, gestión lógica del programa, etc. La programación de este proyecto, implica la solución de desafíos técnicos, desde la integración de API para obtener los datos climáticos hasta la visualizaión de la información.
En resumen, codificar una estación meteorológica como un proyecto ofrece una manera efectiva de combinar teoría y práctica, para el desarrollo de habilidades en la programación.

Este programa es un buscador de condiciones climáticas en un lugar determinado por el usuario, contando con una interfaz gráfica para hacer de la consulta algo más sencillo y comprensible. Los datos serán recabados desde una API y mostrados gráficamnete al usuario.


Algoritmo:
1. Obtener la API de donde se recabarán los datos, en este caso, serán desde OpenWeatherMap.
2. Importar las librerías request para poder extraer información de la API y datetime para poder manejar adecuadamente las undiades de tiempo, mediante import <nombre_libreria>
3. Crear la función que accede a la información de la API y, mediante una estructura de control informa si hay algún error.
4. Crear función para extraer la longitud y latitud del lugar indicado por el usuario.
5. Crear función que extrae los datos del clima: temperatura en Celsius, temperatura en Fahrenheit (en esta parte se utilizarán operadores matemáticos para realizar la conversión), temperatura en Kelvins (en esta parte igual se utilizarán operadores matemáticos para realizar la conversión), humedad, temperatura máxima, mínima y su promedio.
6. Crear la función que extraerá la velocidad del viento.
7. Mediante una estructura de control y, asegurándose que no hay algún error en la API, se imprimen los datos de la ciudad indicada por el usuario.

Desde la vista del usuario, el programa pregunta la ciudad de la cual se requiere conocer los datos meteorológicos, el usuario teclea el nombre de la ciudad y, el programa devuelve el nombre de la ciudad, la longitud, latitud, Temperatura en grados Celsius, Temperatura en grados Fahrenheit, Temperatura en grados Kelvin, Humedad, Temperatura Mínima, Temperatura Máxima, Promedio de temperatura y Viento obtenidos desde una API.
