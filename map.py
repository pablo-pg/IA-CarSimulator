# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Clase Map

import numpy

class Map:
  def __init__(self, h_size, v_size):
    self.h_size = h_size
    self.v_size = v_size
    self.matrix = numpy.zeros(shape=(h_size, v_size))


test = Map(3,5)
test.matrix[0][1] = 3
print(test.matrix)
