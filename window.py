# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Funciones generadoras de ventanas.

from tkinter import *
#from buttons import PassToWindow2
from map import *

def FirstWindow(root, Window1):
  VariableRandom = BooleanVar() # True - Random, False - Manual
  VariableLoad = BooleanVar() # True - Load, False - Create

  RuteText = StringVar()

  WidthText = IntVar()
  HeightText = IntVar()

  PercentageText = IntVar()
  CoordsText = StringVar()
   
  # Frame que contiene al de la izq y dcha
  Frame3 = Frame(Window1)
  Frame3.pack(side=TOP, expand="True",fill=BOTH)
  
  # Boton en la parte inferior
  NextButton = Button(Window1, text="Siguiente", bg="#C2E7C1", command=lambda: PassToWindow2(root, Window1, VariableRandom, VariableLoad, RuteText, WidthText, HeightText, PercentageText, CoordsText))
  NextButton.pack(side=BOTTOM, expand="True",fill=BOTH)

  # Frame de la izquierda
  Frame1 = Frame(Frame3)
  Frame1.pack(expand="True",fill=BOTH, side=LEFT)
  Frame1.config(bg='#F2F3F9')

  LoadMapLabel = Label(Frame1, text="Cargar un mapa desde txt", pady=10, padx=10)
  LoadMapLabel.config(font=('Bookman', 20))
  LoadMapLabel.grid(row=0, sticky=N, columnspan=2)

  LoadButton = Radiobutton(Frame1, text="Cargar", font=('Courier',16), variable=VariableLoad, value=True)
  LoadButton.grid(row=1, sticky=N, columnspan=2)

  IntroduceRuteLabel = Label(Frame1, text="Ruta:", font=('Bookman', 14), pady=5)
  IntroduceRuteLabel.grid(row=2, column=0, sticky=E, padx=2)
  RuteTextBox = Entry(Frame1, textvariable=RuteText)
  RuteTextBox.grid(row=2, column=1, sticky=W, padx=2)

  # Frame de la derecha
  Frame2 = Frame(Frame3)
  Frame2.pack(expand="True",fill=BOTH, side=RIGHT)
  Frame2.config(bg='#E5E6E9')

  CreateMapLabel = Label(Frame2, text="Crear un mapa de MxN", pady=10)
  CreateMapLabel.grid(row=0, sticky=N, columnspan=3)
  CreateMapLabel.config(font=('Bookman', 20))

  WidthLabel = Label(Frame2, text="Ancho del mapa:", font=('Bookman', 14), pady=5)
  WidthLabel.grid(row=2, column=0, sticky=W, padx=2)
  WidthTextBox = Entry(Frame2, textvariable=WidthText)
  WidthTextBox.grid(row=2, column=1, sticky=W, padx=2)

  HeightLabel = Label(Frame2, text="Alto del mapa:", font=('Bookman', 14), pady=5)
  HeightLabel.grid(row=3, column=0, sticky=W, padx=2)
  HeightTextBox = Entry(Frame2, textvariable=HeightText)
  HeightTextBox.grid(row=3, column=1, sticky=W, padx=2)

  ObstacleLabel = Label(Frame2, text="Obstaculos:", font=('Bookman', 14), pady=5)
  ObstacleLabel.grid(row=5, sticky=W)

  RandomButton = Radiobutton(Frame2, text="Aleatorios", variable=VariableRandom, value = True, padx=8,font=('Courier', 12))
  RandomButton.grid(row=6, column=0, sticky=W)
  PercentageLabel = Label(Frame2, text="Porcentaje en %:")
  PercentageLabel.grid(row=6, column=1, sticky=E, padx=2)
  PercentageTextBox = Entry(Frame2, textvariable=PercentageText)
  PercentageTextBox.grid(row=6, column=2, sticky=W, padx=2)


  ManualButton = Radiobutton(Frame2, text="Manuales", variable=VariableRandom, value = False, padx=8,font=('Courier', 12))
  ManualButton.grid(row=8, column=0, sticky=W)
  CoordsLabel = Label(Frame2, text="Coordenadas\n(x1, y1) (x2, y2)")
  CoordsLabel.grid(row=8,column=1, sticky=E, padx=2)
  CoordsTextBox = Entry(Frame2, textvariable=CoordsText)
  CoordsTextBox.grid(row=8, column=2, sticky=W, padx=2)

  CreateButton = Radiobutton(Frame2, text="Crear", font=('Courier',16), variable=VariableLoad, value=False)
  CreateButton.grid(row=1, sticky=N, columnspan=3)

  # CreateMapButton = Button(Frame2, text="Crear mapa") # Añadir command
  # CreateMapButton.grid(row=9, sticky=N, columnspan=3)

  return HeightText, WidthText

def SecondWindow(root, window2, test_map):
  #root2 = Toplevel()
  Frame1 = Frame(window2)
  Frame1.pack(expand="True",fill=BOTH, side=LEFT)
  Frame1.config(bg='#F2F3F9')

  for r in range(0, test_map.v_size):
    for c in range (0, test_map.h_size):
      square = Button(Frame1, text='({},{})'.format(r,c), activebackground="black", background="white")
      square.grid(row=r, column=c)

def PassToWindow2(root,window1,VariableRandom, VariableLoad, RuteText, WidthText, HeightText, PercentageText, CoordsText):
  # Aquí se generara el mapa
  VariableRandom_info = VariableRandom.get()
  VariableLoad_info = VariableLoad.get()
  RuteText_info = RuteText.get()

  WidthText_info = WidthText.get()
  HeightText_info = HeightText.get()

  PercentageText_info = PercentageText.get()
  CoordsText_info = CoordsText.get()

  print("Prueba: " + str(VariableRandom_info) + " " + str(VariableLoad_info) + " " + str(RuteText_info) + " " + str(WidthText_info) + " " + str(HeightText_info) + " " + str(PercentageText_info) + " " + str(CoordsText_info))
  
  # Crear aqui el mapa con las condiciones que se han pasado.
  if (VariableLoad==True):
    # Se lee el mapa y lo retorna a una variable
    test_map = ReadMap(RuteText_info) # No implementado
  
  else: # Se genera con los datos pasados
    # map() constructor. Hacer
    # Condiciones de los obtaculos
    if (VariableRandom_info):
      print("Random")
    else: # Se entran manual
      # Si me sale bien lo de clickar, quitamos esta opcion
      print("hola")

  # Evolucion de ventanas
  window1.destroy() # Cierra la ventana anterior
  Window2 = Toplevel(root) # Se genera la siguiente ventana
  test_map = Map(20, 15)
  SecondWindow(root, Window2, test_map)


# Funcion para leer el mapa desde el txt
def ReadMap(RuteText):
  # No está probado todavía
  with open(str(RuteText)) as f:
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
      print("hola")
  return #retorna el mapa generado