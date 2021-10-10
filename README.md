# IA-CarSimulator

## Índice
- [Introducción](#introducción).
- [Ejecución](#ejecución).
- [Detalles de implementación](#detalles-de-implementación).
- [Formato del fichero de datos](#formato-del-fichero-de-datos).
- [Miembros](#miembros).
- [Referencias](#referencias)


## Introducción
Como primera práctica de la asignatura Inteligencia Artificial, debimos programar un agente inteligente capaz de encontrar el camino más corto en un mundo con obstáculos.

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

## Formato del fichero de datos
Primera línea:  
alto_del_mapa ancho_del_mapa  
Siguientes líneas. Obstáculos:  
CoordX CoordY  
CoordX CoordY  

## Miembros
Helena García Díaz (alu0100829150@ull.edu.es)  
Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
Pablo Pérez González (alu0101318318@ull.edu.es)

## Referencias
[Página oficial de Python](https://www.python.org/)  
[La librería Tkinter: Documentación oficial](https://docs.python.org/es/3/library/tkinter.html)  
[Página oficial de la librería PIL (Pillow Imaging Library)](https://pypi.org/project/Pillow/)  
[Repositorio de este software](https://github.com/pablo-pg/IA-CarSimulator.git)