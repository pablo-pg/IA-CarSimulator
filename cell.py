# Simulador del grupo 10
# Miembros: 
#     Helena García Díaz (alu0100829150@ull.edu.es)  
#     Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
#     Pablo Pérez González (alu0101318318@ull.edu.es)
#
# Clase Cell. Cada coordenada del mapa será una instancia de celdas

class Cell:

  id = 0          # Cada celda tendrá su propio ID, se empieza a contar desde 0
  
  def __init__(self, x_pos, y_pos, is_obstacle = False, is_origin = False, is_finish = False):
      self.id = Cell.id
      self.x_pos = x_pos              # Posición horizontal de la celda
      self.y_pos = y_pos              # Posición vertical de la celda
      self.is_obstacle = is_obstacle  # True si contiene un obstáculo
      self.is_origin = is_origin
      self.is_finish = is_finish
      
      Cell.id += 1      # Aumenta el ID conforme se crean más celdas

  def isObstacle(self):
    return self.is_obstacle
  
  def isOrigin(self):
    return self.is_origin
  
  def isFinish(self):
    return self.is_finish



