# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Funciones generadoras de ventanas.

from cell import Cell
from typing import Type

class Node:
  def __init__ (self, cell_from: Type[Cell], parent=None):
    # print(type(cell))
    self.cell = cell_from # point
    self.cell
    self.parent = parent
    self.H = 0
    self.G = 0
    self.F = 0
    self.id = cell_from.id
  
  def __eq__(self, other):
    return self.cell.id == other.cell.id
  
  # def ManhattanDistance(self, x_pos, y_pos):
  #   return self.cell.manhattanDistance(x_pos, y_pos)