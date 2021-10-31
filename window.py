# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Funciones generadoras de ventanas.

from tkinter import *
#from buttons import PassToWindow2
from map import *
from PIL import Image, ImageTk
from car import Car

def FirstWindow(root, Window1):
  VariableRandom = BooleanVar() # True - Random, False - Manual
  VariableLoad = BooleanVar() # True - Load, False - Create
  VariableRandom.set(True)
  VariableLoad.set(True)

  RuteText = StringVar()
  RuteText.set("mapa1.txt")

  WidthText = IntVar()
  WidthText.set(10)
  HeightText = IntVar()
  HeightText.set(10)

  PercentageText = IntVar()
  PercentageText.set(25)

  OriginXText = IntVar()
  OriginXText.set(0)
  OriginYText = IntVar()
  OriginYText.set(0)

  FinishXText = IntVar()
  FinishXText.set(7)
  FinishYText = IntVar()
  FinishYText.set(7)
   
  # Frame que contiene al de la izq y dcha
  Frame3 = Frame(Window1)
  Frame3.pack(side=TOP, expand="True",fill=BOTH)
  
  # Botones en la parte inferior
  ExitButton = Button(Window1, text="Salir del programa", bg="#E49795", command=ExitProgram)
  ExitButton.pack(side=BOTTOM, expand="True", padx=5)

  NextButton = Button(Window1, text="Siguiente", bg="#C2E7C1", command=lambda: PassToWindow2(root, Window1, VariableRandom, VariableLoad, RuteText, WidthText, HeightText, PercentageText, CoordsTextBox, OriginXText, OriginYText, FinishXText, FinishYText))
  NextButton.pack(side=BOTTOM, expand="True", padx=5)

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
  CoordsLabel = Label(Frame2, text="Coordenadas\nx1 y1\nx2 y2")
  CoordsLabel.grid(row=8,column=1, sticky=E, padx=2)
  CoordsTextBox = Text(Frame2, width=16,height=5)#,textvariable=CoordsText)
  CoordsTextBox.grid(row=8, column=2, sticky=W, padx=2)
  scrollVert=Scrollbar(Frame2, command=CoordsTextBox.yview)
  scrollVert.grid(row=8, column=2, padx=2, sticky="nse")
  CoordsTextBox.config(yscrollcommand=scrollVert.set)

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
  Frame0 = Frame(window2)
  Frame0.pack(expand="True", fill=BOTH, side=TOP)

  Canvas1 = Canvas(Frame0)
  ScrollBarVertical =Scrollbar(Frame0, orient="vertical", command=Canvas1.yview)
  ScrollBarVertical.pack(side="right", fill="y")

  ScrollBarHorizontal = Scrollbar(Frame0, orient="horizontal", command=Canvas1.xview)
  ScrollBarHorizontal.pack(side="bottom", fill="x")

  Frame1 = Frame(Canvas1)

  Frame1.bind(
    "<Configure>",
    lambda e: Canvas1.configure(
      scrollregion = Canvas1.bbox("all")
    )
  )
  Canvas1.create_window((0,0), window=Frame1, anchor="nw")
  Canvas1.configure(yscrollcommand=ScrollBarVertical.set)
  Canvas1.configure(xscrollcommand=ScrollBarHorizontal.set)
  Canvas1.pack(side="left", fill="both", expand=True)
 
  Frame2 = Frame(window2)
  Frame2.pack(side=BOTTOM)

  NextButton = Button(Frame2, text="Siguiente", bg="#C2E7C1", command=lambda: PassToWindow3(root, window2, maps)) # Implementar la siguiente ventana
  NextButton.pack(side=RIGHT, expand="True",fill=BOTH, padx=5)

  ExitButton = Button(Frame2, text="Salir del programa", bg="#E49795", command=ExitProgram)
  ExitButton.pack(side=LEFT, expand="True",fill=BOTH, padx=5)

  if (maps[0].v_size > 35) | (maps[0].h_size > 35):
    maps[0].print()
    image1 = Image.open("map1.jpg")
    image1.show()
    image1= image1.resize((10*maps[0].h_size,10*maps[0].v_size))
    render = ImageTk.PhotoImage(image1)
    img = Label(Frame1, image=render)
    img.render = render
    img.pack(expand="False", fill=BOTH, side=TOP)
  else:
    for r in range(0, maps[0].v_size):
      for c in range (0, maps[0].h_size):
        Draw_Map(Frame1,maps, r, c)
  

def ThirdWindow(root, Window3, maps):
  VariableEvaluate = BooleanVar() # True -> Evaluar todas las func. False -> Evaluar seleccion
  VariableDirections = BooleanVar() # True -> Todas las direcciones. False -> Elegir
  VariableEvaluate.set(True)
  VariableDirections.set(True)

  # Botones en la parte inferior
  ExitButton = Button(Window3, text="Salir del programa", bg="#E49795", command=ExitProgram)
  ExitButton.pack(side=BOTTOM, expand="True", padx=5)

  NextButton = Button(Window3, text="Siguiente", bg="#C2E7C1", command=lambda: PassToWindow4(root, Window3, maps)) # Implementar pantalla de muestra de resultados
  NextButton.pack(side=BOTTOM, expand="True", padx=5)
  
  # Estructura superior de la ventana
  Frame1 = Frame (Window3)
  Frame1.pack(side=TOP)
  
  # Direcciones
  DirectionsLabel = Label(Frame1, text="Definir el número de direcciones")
  DirectionsLabel.config(font=('Bookman', 20))
  DirectionsLabel.grid(row=0, columnspan=4, sticky=N, pady=10, padx=10)

  EvaluateAllDirectionsButton = Radiobutton(Frame1, text="Evaluar todas", font=('Courier',16), variable=VariableDirections, value=True)
  EvaluateAllDirectionsButton.grid(row=2, sticky=N, column=1, padx=5)

  EvaluateSelectionDirectionsButton = Radiobutton(Frame1, text="Evaluar Seleccion", font=('Courier',16), variable=VariableDirections, value=False)
  EvaluateSelectionDirectionsButton.grid(row=2, sticky=N, column=3, padx=5)

  Directions4 = IntVar()
  Directions8 = IntVar()
  Checkbutton(Frame1, text="4 direcciones", variable=Directions4).grid(row=3, sticky=N, column=3, padx=2)
  Checkbutton(Frame1, text="8 direcciones", variable=Directions8).grid(row=4, sticky=N, column=3, padx=2)

  # Funciones
  FunctionsLabel = Label(Frame1, text="Definir función(es) heurística(s)")
  FunctionsLabel.config(font=('Bookman', 20))
  FunctionsLabel.grid(row=10, columnspan=4, sticky=N, pady=10, padx=10)
  Label(Frame1, text="(Solo se aplicarán las correctas\n según el número de direcciones seleccionado)").grid(row=11, sticky=N, columnspan=4, pady=2)

  EvaluateAllButton = Radiobutton(Frame1, text="Evaluar todas", font=('Courier',16), variable=VariableEvaluate, value=True)
  EvaluateAllButton.grid(row=12, sticky=N, column=1, padx=5)

  EvaluateSelectionButton = Radiobutton(Frame1, text="Evaluar selección", font=('Courier',16), variable=VariableEvaluate, value=False)
  EvaluateSelectionButton.grid(row=12, sticky=N, column=3, padx=5)

  Function1 = IntVar()
  Function2 = IntVar()
  Function3 = IntVar()
  Checkbutton(Frame1, text="Distancia Manhatan", variable=Function1).grid(row=13, sticky=N, column=3, padx=2)
  Checkbutton(Frame1, text="Distancia euclídea", variable=Function2).grid(row=14, sticky=N, column=3, padx=2)
  Checkbutton(Frame1, text="Funcion 3", variable=Function3).grid(row=15, sticky=N, column=3, padx=2)
  
def FourthWindow(root, Window4, maps):
  Frame0 = Frame(Window4)
  Frame0.pack(side=TOP)
  maps[0].print()


# Aquí se reciben los datos de la ventana 1. 
# Con esto, se genera el mapa con la info introducida
def PassToWindow2(root,window1,VariableRandom, VariableLoad, RuteText, WidthText, HeightText, PercentageText, CoordsTextBox, OriginXText, OriginYText, FinishXText, FinishYText):
  # Aquí se generara el mapa
  VariableRandom_info = VariableRandom.get()
  VariableLoad_info = VariableLoad.get()
  RuteText_info = RuteText.get()

  WidthText_info = WidthText.get()
  HeightText_info = HeightText.get()

  PercentageText_info = PercentageText.get()

  OriginXText_info = OriginXText.get()
  OriginYText_info = OriginYText.get()

  FinishXText_info = FinishXText.get()
  FinishYText_info = FinishYText.get()

  InputValue=CoordsTextBox.get("1.0","end-1c")

  print("Cuadro de texto: ",InputValue)

  #print("Prueba: " + str(VariableRandom_info) + " " + str(VariableLoad_info) + " " + str(RuteText_info) + " " + str(WidthText_info) + " " + str(HeightText_info) + " " + str(PercentageText_info) + " " + str(CoordsText_info))
  
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
      map1.setDistances()
      map1.generateRandommap(20)
    else: # Se entran manual
      # Si me sale bien lo de clickar, quitamos esta opcion
      print("Manual")
      map1 = Map(WidthText_info, HeightText_info, OriginXText_info, OriginYText_info, FinishXText_info, FinishYText_info)
      map1 = ReadObstacles(InputValue, map1)
      map1.setDistances()
  maps.append(map1)

  # Evolucion de ventanas
  window1.destroy() # Cierra la ventana anterior
  Window2 = Toplevel(root) # Se genera la siguiente ventana
  Window2.title("Estrategias de búsqueda")
  Window2.geometry("500x500")
  SecondWindow(root, Window2, maps)

# Se reciben los datos de la ventana 2 y se genera la tercera ventana
def PassToWindow3(root, window2, maps):
  window2.destroy()
  window3 = Toplevel(root)
  window3.title("Estrategias de búsqueda")
  window3.geometry("500x500")
  ThirdWindow(root, window3, maps)

def PassToWindow4(root, window3, maps):
  car1 = Car(maps[0]) # Cuando funcione pasarle las variables
  car1.algorithm()
  window3.destroy()
  window4 = Toplevel(root)
  window4.title("Estrategias de búsqueda")
  window4.geometry("500x500")
  FourthWindow(root, window3, maps)

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
      map1.setDistances()
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
      # print("X obstaculo: ", XCoord, "Y obstaculo: ", YCoord)
      # XCoord=int(XCoord)
      # YCoord=int(YCoord)
      print(obstacles)
      map1.SetObstacle(XCoord, YCoord)
      # print(f"Añadido en {XCoord},{YCoord}")
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
      # print("X obstaculo: ", XCoord, "Y obstaculo: ", YCoord)
      # XCoord=int(XCoord)
      # YCoord=int(YCoord)
      print(obstacles)
      map1.SetObstacle(XCoord, YCoord)
      # print(f"Añadido en {XCoord},{YCoord}")
      map1.obsCount()
      # map1.print()
    linecount += 1
  return map1

def ReadObstacles(InputValue, map1):
  linecount = 0
  
  for line in InputValue.splitlines():
    lettercount = 0
    XCoord=""
    YCoord=""
    #obstacles = []
    for letter in line:
      if (letter != ' ') and (letter != "\n"):
        if (lettercount == 0):
          XCoord += letter
        else:
          YCoord += letter     
      else:
        lettercount += 1
    XCoord = int(XCoord)
    YCoord = int(YCoord)
    #obstacles.append([XCoord, YCoord])
    # print("Lettercount: ", lettercount)
    # print("Linecount: ", linecount)
    # print("X obstaculo: ", XCoord, "Y obstaculo: ", YCoord)
    #print(obstacles)
    #print("Prueba: ",XCoord >= map1.h_size, YCoord >= map1.v_size,XCoord < 0,YCoord < 0)
    if (XCoord >= map1.h_size) | (YCoord >= map1.v_size):
      print(f"Obstaculo fuera de rango: {XCoord},{YCoord}")
    elif (XCoord < 0) | (YCoord < 0):
      print(f"Obstaculo fuera de rango: {XCoord},{YCoord}")
    else:
      map1.SetObstacle(XCoord, YCoord)
      # print(f"Añadido en {XCoord},{YCoord}")
      #map1.obsCount()
    # map1.print()
    linecount += 1
  return map1

def ChangueToNext(square, Frames, maps, r, c):
  #print("r, c", r, c)
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