# Simulador del grupo 10
# Miembros: 
#     Helena García Díaz (alu0100829150@ull.edu.es)  
#     Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
#     Pablo Pérez González (alu0101318318@ull.edu.es)
#
# Clase Car. Se ocupará de todo el algoritmo y lo referido al movimiento del vehiculo.


class Car:
  def __init__(self, x_origin, y_origin, maps):
    self.x_pos = x_origin
    self.y_pos = y_origin
    maps = maps

  def move(self):
    pass

  def f(self):
    return self.heuristic() + self.g()

  def g(self):
    pass

  def heuristic(self):
    pass