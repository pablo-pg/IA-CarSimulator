# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Funciones generadoras de ventanas.
class Node:
  def __init__ (self, cell=None, parent=None):
    self.cell = cell # point
    self.parent = parent
    self.H = 0
    self.G = 0
    self.F = 0
  
  def __eq__(self, other):
    return self.cell.id == other.cell.id