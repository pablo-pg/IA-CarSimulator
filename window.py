# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Funciones generadoras de ventanas.

from tkinter import *
#from buttons import PassToWindow2
from map import *
from PIL import Image

def FirstWindow(root, Window1):
  VariableRandom = BooleanVar() # True - Random, False - Manual
  VariableLoad = BooleanVar() # True - Load, False - Create

  RuteText = StringVar()
  RuteText.set("mapa1.txt")

  WidthText = IntVar()
  WidthText.set(5)
  HeightText = IntVar()
  HeightText.set(5)

  PercentageText = IntVar()
  CoordsText = StringVar()

  OriginXText = IntVar()
  OriginXText.set(0)
  OriginYText = IntVar()
  OriginYText.set(0)

  FinishXText = IntVar()
  FinishXText.set(3)
  FinishYText = IntVar()
  FinishYText.set(3)
   
  # Frame que contiene al de la izq y dcha
  Frame3 = Frame(Window1)
  Frame3.pack(side=TOP, expand="True",fill=BOTH)
  
  # Boton en la parte inferior
  NextButton = Button(Window1, text="Siguiente", bg="#C2E7C1", command=lambda: PassToWindow2(root, Window1, VariableRandom, VariableLoad, RuteText, WidthText, HeightText, PercentageText, CoordsText, OriginXText, OriginYText, FinishXText, FinishYText))
  NextButton.pack(side=BOTTOM, expand="True", padx=5)

  ExitButton = Button(Window1, text="Salir del programa", bg="#E49795", command=ExitProgram)
  ExitButton.pack(side=BOTTOM, expand="True", padx=5)

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
  #CoordsLabel = Label(Frame2, text="Coordenadas\n(x1, y1) (x2, y2)")
  #CoordsLabel.grid(row=8,column=1, sticky=E, padx=2)
  #CoordsTextBox = Entry(Frame2, textvariable=CoordsText)
  #CoordsTextBox.grid(row=8, column=2, sticky=W, padx=2)

  CreateButton = Radiobutton(Frame2, text="Crear", font=('Courier',16), variable=VariableLoad, value=False)
  CreateButton.grid(row=1, sticky=N, columnspan=3)

  # ORIGEN
  OriginLabel = Label(Frame2, text="Origen:", font=('Bookman', 14), pady=5)
  OriginLabel.grid(row=9, column=0, sticky=W)

  OriginXLabel = Label(Frame2, text="Coordena X:", font=('Bookman', 12), padx=2)
  OriginXLabel.grid(row=10, column=0)
  OriginXTextBox = Entry(Frame2, textvariable=OriginXText)
  OriginXTextBox.grid(row=10, column=1, sticky=W)

  OriginYLabel = Label(Frame2, text="Coordena Y:", font=('Bookman', 12), padx=2)
  OriginYLabel.grid(row=11, column=0)
  OriginYTextBox = Entry(Frame2, textvariable=OriginYText)
  OriginYTextBox.grid(row=11, column=1, sticky=W)

  # DESTINO
  FinishLabel = Label(Frame2, text="Destino:", font=('Bookman', 14), pady=5)
  FinishLabel.grid(row=12, column=0, sticky=W)

  FinishXLabel = Label(Frame2, text="Coordena X:", font=('Bookman', 12), padx=2)
  FinishXLabel.grid(row=13, column=0)
  FinishXTextBox = Entry(Frame2, textvariable=FinishXText)
  FinishXTextBox.grid(row=13, column=1, sticky=W)

  FinishYLabel = Label(Frame2, text="Coordena Y:", font=('Bookman', 12), padx=2)
  FinishYLabel.grid(row=14, column=0)
  FinishYTextBox = Entry(Frame2, textvariable=FinishYText)
  FinishYTextBox.grid(row=14, column=1, sticky=W)


# En la segunda ventana se muestra el mapa interactivo.
# Se podrá editar los obstáculos y puntos de partida y llegada.
def SecondWindow(root, window2, maps):
  # Para ver el mapa generado antes de implementar la interfaz
  #maps[0].print()
  #root2 = Toplevel()
  Frame1 = Frame(window2)
  Frame1.pack(expand="True", side=TOP)
  Frame1.config(bg='#F2F3F9', height="200", width="500")
  
  ScrollBar1 = Scrollbar(window2, orient=HORIZONTAL)
  ScrollBar1.pack(side=BOTTOM, fill=X)
  ScrollBar2 = Scrollbar(window2, orient=VERTICAL)
  ScrollBar2.pack(side=RIGHT, fill=Y)

  Frame2 = Frame(window2)
  Frame2.pack(side=BOTTOM)

  NextButton = Button(Frame2, text="Siguiente", bg="#C2E7C1") # Implementar la siguiente ventana
  NextButton.pack(side=RIGHT, expand="True",fill=BOTH, padx=5)

  ExitButton = Button(Frame2, text="Salir del programa", bg="#E49795", command=ExitProgram)
  ExitButton.pack(side=LEFT, expand="True",fill=BOTH, padx=5)

  if (maps[0].v_size > 35) | (maps[0].h_size > 35):
    maps[0].print()
    image1 = Image.open("F:\AA A Ingeniería Informática\IA\Practica_1_CarSimulator\IA-CarSimulator\map1.jpg")
    render = PhotoImage(image1)
    render = render.resize((50 * maps[0].h_size, 50 * maps[0].v_size), Image.NEAREST)
    img = Label(Frame1, image=render)
    img.pack()   
  else:
    for r in range(0, maps[0].v_size):
      for c in range (0, maps[0].h_size):
        Draw_Map(Frame1,maps, r, c)
  
  
# Aquí se reciben los datos de la ventana 1. 
# Con esto, se genera el mapa con la info introducida
def PassToWindow2(root,window1,VariableRandom, VariableLoad, RuteText, WidthText, HeightText, PercentageText, CoordsText, OriginXText, OriginYText, FinishXText, FinishYText):
  # Aquí se generara el mapa
  VariableRandom_info = VariableRandom.get()
  VariableLoad_info = VariableLoad.get()
  RuteText_info = RuteText.get()

  WidthText_info = WidthText.get()
  HeightText_info = HeightText.get()

  PercentageText_info = PercentageText.get()
  CoordsText_info = CoordsText.get()

  OriginXText_info = OriginXText.get()
  OriginYText_info = OriginYText.get()

  FinishXText_info = FinishXText.get()
  FinishYText_info = FinishYText.get()

  print("Prueba: " + str(VariableRandom_info) + " " + str(VariableLoad_info) + " " + str(RuteText_info) + " " + str(WidthText_info) + " " + str(HeightText_info) + " " + str(PercentageText_info) + " " + str(CoordsText_info))
  
  # Crear aqui el mapa con las condiciones que se han pasado.
  maps = []
  if (VariableLoad_info==True):
    # Se lee el mapa y lo retorna a una variable
    print("Lee el mapa")
    map1 = ReadMap(RuteText_info)
  else: # Se genera con los datos pasados
    # Condiciones de los obtaculos
    if (VariableRandom_info):
      print("Random")
      map1 = Map(WidthText_info, HeightText_info, OriginXText_info, OriginYText_info, FinishXText_info, FinishYText_info)
      map1.generateRandommap(20)
    else: # Se entran manual
      # Si me sale bien lo de clickar, quitamos esta opcion
      print("Manual")
  maps.append(map1)

  # Evolucion de ventanas
  window1.destroy() # Cierra la ventana anterior
  Window2 = Toplevel(root) # Se genera la siguiente ventana
  Window2.title("Estrategias de búsqueda")
  Window2.geometry("500x500")
  SecondWindow(root, Window2, maps)

# Funcion para leer el mapa desde el txt
def ReadMap(RuteText):
  # No está probado todavía
  with open(str(RuteText)) as f:
    lines = f.readlines()

  linecount = 0
  lettercount = 0

  Height=""
  Width=""
  XOrigin=""
  YOrigin=""
  XFinish=""
  YFinish=""

  for line in lines:
    if (linecount == 0): # Lee el tamaño del mapa
      for letter in line:
        if (letter != ' '):
          if (lettercount == 0):
            Height += letter
          else:
            Width += letter
        else:
          lettercount += 1
        # print("Lettercount: ", lettercount)
        # print("Alto: ", Height, "Ancho: ", Width)
    elif (linecount == 1): # Lee las coordenadas de inicio
      lettercount = 0
      for letter in line:
        if (letter != ' '):
          if (lettercount == 0):
            XOrigin += letter
          else:
            YOrigin += letter
        else:
          lettercount += 1
        # print("Lettercount: ", lettercount)
        # print("X Origen: ", XOrigin, "Y Origen: ", YOrigin)
    elif (linecount == 2): # Lee las coordenadas de destino
      lettercount = 0
      for letter in line:
        if (letter != ' '):
          if (lettercount == 0):
            XFinish += letter
          else:
            YFinish += letter
        else:
          lettercount += 1
        # print("Lettercount: ", lettercount)
        # print("X Finish: ", XFinish, "Y Finish: ", YFinish)
    elif (linecount == 3): # Crea el mapa y lee el primer obstáculo
      lettercount = 0
      Height = int(Height)
      Width = int (Width)
      XOrigin = int(XOrigin)
      YOrigin = int(YOrigin)
      XFinish = int(XFinish)
      YFinish = int(YFinish)
      # Creo el mapa para poder asignar los obstáculos
      map1 = Map(Width, Height, XOrigin, YOrigin, XFinish, YFinish)
      # obstaculos
      obstacles = []
      XCoord=""
      YCoord=""
      for letter in line:
        if (letter != ' ') and (letter != "\n"):
          if (lettercount == 0):
            XCoord += letter
          else:
            YCoord += letter     
        else:
          lettercount += 1
      obstacles.append([XCoord, YCoord])
      # print("Lettercount: ", lettercount)
      # print("Linecount: ", linecount)
      print("X obstaculo: ", XCoord, "Y obstaculo: ", YCoord)
      # XCoord=int(XCoord)
      # YCoord=int(YCoord)
      print(obstacles)
      map1.SetObstacle(XCoord, YCoord)
      print(f"Añadido en {XCoord},{YCoord}")
      map1.obsCount()
    else: # Lee el resto de obstáculos
      lettercount = 0
      XCoord=""
      YCoord=""
      for letter in line:
        if (letter != ' ') and (letter != "\n"):
          if (lettercount == 0):
            XCoord += letter
          else:
            YCoord += letter     
        else:
          lettercount += 1
      obstacles.append([XCoord, YCoord])
      # print("Lettercount: ", lettercount)
      # print("Linecount: ", linecount)
      print("X obstaculo: ", XCoord, "Y obstaculo: ", YCoord)
      # XCoord=int(XCoord)
      # YCoord=int(YCoord)
      print(obstacles)
      map1.SetObstacle(XCoord, YCoord)
      print(f"Añadido en {XCoord},{YCoord}")
      map1.obsCount()
      # map1.print()
    linecount += 1
  return map1

def ChangueToNext(square, Frames, maps, r, c):
  print("r, c", r, c)
  # Verde -> Rojo (si no hay ya uno) -> Blanco -> Negro
  if maps[0].matrix[maps[0].pos(c,r)].isOrigin() == True:
    maps[0].matrix[maps[0].pos(c,r)].setWhite()
    # Comprueba si ya hay un destino
    finish = CheckFinish(maps[0])
    if finish == False:
      maps[0].matrix[maps[0].pos(c,r)].setFinish()
    # else: se convierte en blanco
  elif maps[0].matrix[maps[0].pos(c,r)].isFinish() == True:
    maps[0].matrix[maps[0].pos(c,r)].setWhite()
  elif maps[0].matrix[maps[0].pos(c,r)].isObstacle() == True:
    maps[0].matrix[maps[0].pos(c,r)].setWhite()
    # Comprueba si ya hay un origen
    Origin = CheckOrigin(maps[0])
    if Origin == False:
      maps[0].matrix[maps[0].pos(c,r)].setOrigin()
    # Pasa a ver si hay un final
    finish = CheckFinish(maps[0])
    if finish == False:
      maps[0].matrix[maps[0].pos(c,r)].setFinish()
  else: # Es un blanco y pasa a negro
    maps[0].matrix[maps[0].pos(c,r)].setObstacle()
  
  Draw_Map(Frames, maps, r, c)

  Tk.update(Frames)
  Tk.update_idletasks(Frames)
  #refresh(Frames[0])
  #print("Actualizacion")
  #maps[0].print()


def CheckFinish(maps):
  finish = False
  for i in range(maps.h_size):
    for j in range(maps.v_size):
      if maps.matrix[maps.pos(i,j)].isFinish() == True: 
        finish = True
  return finish

def CheckOrigin(maps):
  Origin = False
  for i in range(maps.h_size):
    for j in range(maps.v_size):
      if maps.matrix[maps.pos(i,j)].isOrigin() == True: 
        Origin = True
  return Origin

def Draw_Map(Frame1, maps, r, c):
  if maps[0].matrix[maps[0].pos(c,r)].isOrigin() == True:
        square = Button(Frame1,text="I", activebackground="grey", background="green", height=1, width=2, command=lambda r=r, c=c: ChangueToNext(square, Frame1, maps, r, c)).grid(row=r, column=c)
        # square = Button(Frame1, text='({},{}, {})'.format(r,c, "true"), activebackground="grey", background="green", command=lambda r=r, c=c: ChangueToNext(Frame1, maps, r, c))
  elif maps[0].matrix[maps[0].pos(c,r)].isFinish() == True:
    square = Button(Frame1, text='F',activebackground="grey", background="red", height=1, width=2, command=lambda r=r, c=c: ChangueToNext(square, Frame1, maps, r, c)).grid(row=r, column=c)
    #square = Button(Frame1, text='({},{})'.format(r,c), activebackground="grey", background="red")
  elif maps[0].matrix[maps[0].pos(c,r)].isObstacle() == True:
    square = Button(Frame1, activebackground="grey", background="black", height=1, width=2, command=lambda r=r, c=c: ChangueToNext(square, Frame1, maps, r, c)).grid(row=r, column=c)
    #square = Button(Frame1, text='({},{})'.format(r,c), activebackground="grey", background="black")
  else:
    square = Button(Frame1, activebackground="grey", background="white", height=1, width=2, command=lambda r=r, c=c: ChangueToNext(square, Frame1, maps, r, c)).grid(row=r, column=c)
    #square = Button(Frame1, text='({},{})'.format(r,c), activebackground="grey", background="white")

def ExitProgram():
  raise SystemExit