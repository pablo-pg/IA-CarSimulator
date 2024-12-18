# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Clase Map

import random
from PIL import Image
from cell import Cell



class Map:

  def __init__(self, h_size = 10, v_size = 10, x_origin = 0, y_origin = 0, x_end = 1, y_end = 1):
    if (h_size <= 0):
      self.h_size = 10
    else:
      self.h_size = h_size          # Tamaño horizontal del mapa
    if (v_size <=0):
      self.v_size = 10
    else:
      self.v_size = v_size          # Tamaño vertical del mapa
    self.matrix = []              # Lista que será usada para representar la matriz
    if (x_origin >= h_size) | (x_origin < 0):           
      self.x_origin = 0
    else:
      self.x_origin = x_origin      # Punto de partida del coche
    
    if (y_origin >= v_size) | (y_origin < 0):           
      self.yorigin = 0
    else:
      self.y_origin = y_origin
    
    if (x_end == x_origin | x_end < 0 | x_end >= h_size):
      self.x_end = 1
    else:
      self.x_end = x_end                # Punto de destino del coche
    

    if (y_end == y_origin | y_end < 0 | y_end >= v_size):
      self.y_end = 1
    else:
      self.y_end = y_end
    
    for i in range(v_size):
      for j in range(h_size):
        cell = Cell(j,i)
        self.matrix.append(cell)

    self.matrix[self.pos(self.x_origin, self.y_origin)].is_origin = True
    self.matrix[self.pos(self.x_end, self.y_end)].is_finish = True


  # Devuele la posición real de la lista pasando por parámetro posiciones x,y
  def pos(self, i, j):
    return int(i * self.v_size + j)


  # Genera el mapa con obstáculos aleatorios según el porcentaje de obstáculos deseados
  def generateRandommap(self, percentage):
    size = self.h_size * self.v_size
    obs_number = int(percentage * size / 100)
    for i in range(obs_number):
      rand_pos_x = random.randint(0, self.h_size - 1)
      rand_pos_y = random.randint(0, self.v_size - 1)
      while (rand_pos_x == self.x_origin) or (rand_pos_x == self.x_end):
        rand_pos_x = random.randint(0, self.h_size - 1)
      while (rand_pos_y == self.y_origin) or (rand_pos_y == self.y_end):
        rand_pos_y = random.randint(0, self.v_size - 1)
      self.matrix[self.pos(rand_pos_x, rand_pos_y)].is_obstacle = True


  # Setea obstaculos
  def SetObstacle(self, i, j):
    if (i != self.x_origin and j != self.y_origin) and (i != self.x_end and j != self.y_end):
      self.matrix[self.pos(int(i),int(j))].is_obstacle = True
    else:
      print("No se puede establecer como obstáculo la salida o el destino.\n")


  def obsCount(self):
    count = 0
    for i in self.matrix:
      if i.isObstacle() == True:
        count += 1
    print(f"Hay {count} obstáculos")


  def setDistances(self):
    # for i in self.h_size:
    #   for j in self.v_size:
    #     self.matrix[self.pos(i, j)].euclideanDistance(self.x_end, self.y_end)
    #     self.matrix[self.pos(i, j)].manhattanDistance(self.x_end, self.y_end)
    for cell in self.matrix:
      cell.euclideanDistance(self.x_end, self.y_end)
      cell.manhattanDistance(self.x_end, self.y_end)


  # Genera un PNG con el mapa y sus obstáculos
  def print(self):
    img = Image.new("RGB", (self.h_size, self.v_size))
    pixels = img.load()
    # Recorre todo el mapa y si no hay obstáculo lo pinta de blanco
    for i in range(self.h_size):
        for j in range(self.v_size):
            if self.matrix[self.pos(i,j)].isObstacle() == False:
                pixels[i,j] = (255,255,255)
            if self.matrix[self.pos(i,j)].isOrigin() == True:
              pixels[i,j] = (194, 231, 193)
            if self.matrix[self.pos(i,j)].isFinish() == True:
              pixels[i,j] = (228, 151, 149 )
    # Amplía la imagen
    img = img.resize((50 * self.h_size, 50 * self.v_size), Image.NEAREST)
    img.save('map1.jpg')
  

# mapq = Map(10, 10, 0, 0, 5, 5)
# mapq.setDistances()
# mapq.generateRandommap(20)
# mapq.obsCount()
# mapq.print()
