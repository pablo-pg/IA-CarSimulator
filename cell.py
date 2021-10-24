# Simulador del grupo 10
# Miembros: 
#     Helena García Díaz (alu0100829150@ull.edu.es)  
#     Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
#     Pablo Pérez González (alu0101318318@ull.edu.es)
#
# Clase Cell. Cada coordenada del mapa será una instancia de celdas

import math

class Cell:

  id = 0          # Cada celda tendrá su propio ID, se empieza a contar desde 0
  
  def __init__(self, x_pos, y_pos, is_obstacle = False, is_origin = False, is_finish = False):
      self.id = Cell.id
      self.x_pos = x_pos              # Posición horizontal de la celda
      self.y_pos = y_pos              # Posición vertical de la celda
      self.is_obstacle = is_obstacle  # True si contiene un obstáculo
      self.is_origin = is_origin
      self.is_finish = is_finish
      self.manhattan_distance = math.inf
      self.euclidean_distance = math.inf
      
      Cell.id += 1      # Aumenta el ID conforme se crean más celdas

  def isObstacle(self):
    if self.is_obstacle == True:
      return True
    else:
      return False
  
  def isOrigin(self):
    if self.is_origin == True:
      return True
    else:
      return False
  
  def isFinish(self):
    if self.is_finish == True:
      return True
    else:
      return False

  def setObstacle(self):
    self.is_obstacle = True
  
  def setOrigin(self):
    self.is_origin = True
  
  def setFinish(self):
    self.is_finish = True

  def setWhite(self):
    self.is_origin = False
    self.is_obstacle = False
    self.is_finish = False

  def euclideanDistance(self, x_finish, y_finish):
    if x_finish > self.x_pos:
      x = ((x_finish - self.x_pos)^2)
    else:
      x = ((self.x_pos - x_finish)^2)
    if y_finish > self.y_pos:
      y = ((y_finish - self.y_pos)^2)
    else:
      y = ((self.y_pos - y_finish)^2)
    self.euclidean_distance = math.sqrt(x + y)
    return self.euclidean_distance

  def manhattanDistance(self, x_finish, y_finish):
    self.manhattan_distance = (abs(x_finish - self.x_pos) + abs(y_finish - self.y_pos))
    return self.manhattan_distance
