# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Clase Cell. Cada objeto del mapa será una instancia de celdas

class Cell:
  id = 0
  def __init__(self, x_pos, y_pos, is_obstacle=False):
      self.id = Cell.id
      self.x_pos = x_pos
      self.y_pos = y_pos
      self.is_obstacle = is_obstacle
      
      Cell.id += 1

  def isObstacle(self):
    return self.is_obstacle



