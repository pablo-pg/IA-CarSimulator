# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Funciones generadoras de ventanas.

from tkinter import *

def FirstWindow(root):
  VariableRandom = BooleanVar()

  root.title = "Estrategias de búsqueda"

  # Frame de la izquierda
  Frame1 = Frame()
  Frame1.pack(expand="True",fill=BOTH, side=LEFT)
  Frame1.config(bg='#F2F3F9')

  LoadMapLabel = Label(Frame1, text="Cargar un mapa desde txt")
  LoadMapLabel.grid(row=0, sticky=N, columnspan=2)

  

  IntroduceRuteLabel = Label(Frame1, text="Ruta:" )
  IntroduceRuteLabel.grid(row=1, column=0, sticky=W, padx=2)
  RuteTextBox = Entry(Frame1)
  RuteTextBox.grid(row=1, column=1, sticky=W, padx=2)

  with open(RuteTextBox) as f:
    lines = f.readlines()
  
  linecount = 0
  lettercount = 0
  for line in lines:
    linecount += 1
    if (linecount == 1):
      for letter in line:
        if (letter != ''):
          if (lettercount == 0):
            Height += letter
            Height = int(Height)
          else:
            Width += letter
            Width = int(Width)
        else:
          lettercount = 1
    else:
      # obstaculos

  # LoadMapButton = Button(Frame1, text="Cargar mapa", command=LoadMapAction) # Añadir command
  # LoadMapButton.grid(row=2, sticky=N, columnspan=2)

  # Frame de la derecha
  Frame2 = Frame()
  Frame2.pack(expand="True",fill=BOTH, side=RIGHT)
  Frame2.config(bg='#E5E6E9')

  CreateMapLabel = Label(Frame2, text="Crear un mapa de MxN")
  CreateMapLabel.grid(row=0, sticky=N, columnspan=3)

  WidthLabel = Label(Frame2, text="Ancho del mapa:")
  WidthLabel.grid(row=1, column=0, sticky=W, padx=2)
  WidthTextBox = Entry(Frame2)
  WidthTextBox.grid(row=1, column=1, sticky=W, padx=2)

  HeightLabel = Label(Frame2, text="Alto del mapa:")
  HeightLabel.grid(row=2, column=0, sticky=W, padx=2)
  HeightTextBox = Entry(Frame2)
  HeightTextBox.grid(row=2, column=1, sticky=W, padx=2)

  ObstacleLabel = Label(Frame2, text="Obstaculos:")
  ObstacleLabel.grid(row=4, sticky=W)

  RandomButton = Radiobutton(Frame2, text="Aleatorio", variable=VariableRandom, value = True)
  RandomButton.grid(row=5, column=1, sticky=W)
  PercentageLabel = Label(Frame2, text="Porcentaje en %:")
  PercentageLabel.grid(row=6, column=1, sticky=E, padx=2)
  PercentageTextBox = Entry(Frame2)
  PercentageTextBox.grid(row=6, column=2, sticky=W, padx=2)


  ManualButton = Radiobutton(Frame2, text="Manuales", variable=VariableRandom, value = False)
  ManualButton.grid(row=7, column=1, sticky=W)
  CoordsLabel = Label(Frame2, text="Coordenadas (x1, y1) (x2, y2)")
  CoordsLabel.grid(row=8,column=1, sticky=E, padx=2)
  CoordsTextBox = Entry(Frame2)
  CoordsTextBox.grid(row=8, column=2, sticky=W, padx=2)

  CreateMapButton = Button(Frame2, text="Crear mapa") # Añadir command
  CreateMapButton.grid(row=9, sticky=N, columnspan=3)

  return HeightTextBox, WidthTextBox