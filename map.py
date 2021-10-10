# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Clase Map


from PIL import Image
from cell import Cell



class Map:

  def __init__(self, h_size, v_size):
    self.h_size = h_size          # Tamaño horizontal del mapa
    self.v_size = v_size          # Tamaño vertical del mapa
    self.matrix = []              # Lista que será usada para representar la matriz
    for i in range(v_size):
      for j in range(h_size):
        cell = Cell(j,i)
        self.matrix.append(cell)

  # Devuele la posición real de la lista pasando por parámetro posiciones x,y
  def pos(self, i, j):
    return i * self.v_size + j

  # Genera un PNG con el mapa y sus obstáculos
  def print(self):
    img = Image.new("RGB", (self.h_size, self.v_size))
    pixels = img.load()
    # Recorre todo el mapa y si no hay obstáculo lo pinta de negro
    for i in range(self.h_size):
        for j in range(self.v_size):
            if self.matrix[self.pos(i,j)].isObstacle() == False:
                pixels[i,j] = (255,255,255)
    # Amplía la imagen
    img = img.resize((50 * self.h_size, 50 * self.v_size), Image.NEAREST)
    img.show()

# Testeo de la clase
test = Map(10,15)

test.matrix[test.pos(0,0)].is_obstacle = True
test.matrix[test.pos(0,4)].is_obstacle = True
test.matrix[test.pos(2,2)].is_obstacle = True
test.matrix[test.pos(0,0)].is_obstacle = True
test.matrix[test.pos(5,7)].is_obstacle = True
test.matrix[test.pos(9,14)].is_obstacle = True

test.print()

