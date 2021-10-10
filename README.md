# IA-CarSimulator

## Introducción
Como primera práctica de la asignatura Inteligencia Artificial, debimos programar un agente inteligente capaz de encontrar el camino más corto en un mundo con obstáculos.
## Miembros
Helena García Díaz (alu0100829150@ull.edu.es)  
Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
Pablo Pérez González (alu0101318318@ull.edu.es)

## Ejecución
Sitúese en la carpeta del proeycto y ejecute:  
`$ python3 main.py`

## Detalles de implementación
Lenguaje de programación: Python  
Librerías usadas: tkinter, PIL  
Interfaz de usuario: Gráfica  
**Diseño de clases:**
* Clase Cell: Cada celda almacena su posición y si contiene o no un obstáculo.
* Clase Map: Contiene una lista de celdas que forman una matriz donde el coche
podrá moverse. Se encarga de generar cada una de sus celdas y de generar una imagen que muestre el entorno.

## Formato del txt
Primera línea: 
alto_del_mapa ancho_del_mapa
Siguientes líneas. Obstáculos: 
CoordX CoordY
CoordX CoordY

## Notas