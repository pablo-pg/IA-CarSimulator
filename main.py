# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Main

from tkinter import *
from window import *
from map import *

root = Tk()
root.title("Root")
root.withdraw()

Window1 = Toplevel(root)
Window1.title("Estrategias de búsqueda")
height, width = FirstWindow(root, Window1) # En realidad no tiene sentido que retorne un valor

root.mainloop()
