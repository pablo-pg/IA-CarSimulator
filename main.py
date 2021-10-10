# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Main

from tkinter import *

root = Tk()

root.title = "Estrategias de búsqueda"

Frame1 = Frame()
Frame1.pack(expand="True", side=LEFT)
#Frame1.config(bg='#F2F3F9')

CreateMapLabel = Label(Frame1, text="Crear un mapa de MxN")
CreateMapLabel.pack(side=TOP)

IntroduceRuteLabel = Label(Frame1, text="Ruta:" )
IntroduceRuteLabel.pack(side=LEFT)
RuteTextBox = Entry(Frame1)
RuteTextBox.pack(side= LEFT)


Frame2 = Frame()
Frame2.pack(expand="True", side=RIGHT)
#Frame2.config(bg='#E5E6E9')

CreateMapLabel2 = Label(Frame2, text="Cargar un mapa desde txt")
CreateMapLabel2.pack(side = TOP)

WidthLabel = Label(Frame2, text="Ancho del mapa:")
WidthLabel.pack(side=LEFT)
WidthTextBox = Entry(Frame2)
WidthTextBox.pack(side=LEFT)

HeightLabel = Label(Frame2, text="Alto del mapa:")
HeightLabel.pack(side=LEFT)
HeightTextBox = Entry(Frame2)
HeightTextBox.pack(side=LEFT)

Frame2 = Frame()

root.mainloop()


