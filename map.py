# Simulador del grupo 10
# Miembros: 
# Helena García Díaz (alu0100829150@ull.edu.es)  
# Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
# Pablo Pérez González (alu0101318318@ull.edu.es)
# Clase Map


from PIL import Image
from cell import Cell



class Map:

  def __init__(self, h_size = 10, v_size = 10, x_origin = 0, y_origin = 0, x_end = 1, y_end = 1):
    self.h_size = h_size          # Tamaño horizontal del mapa
    self.v_size = v_size          # Tamaño vertical del mapa
    self.matrix = []              # Lista que será usada para representar la matriz
    self.x_origin = x_origin      # Punto de partida del coche
    self.y_origin = y_origin
    self.x_end = x_end                # Punto de destino del coche
    self.y_end = y_end
    for i in range(v_size):
      for j in range(h_size):
        cell = Cell(j,i)
        self.matrix.append(cell)

    self.matrix[self.pos(x_origin, y_origin)].is_origin = True
    self.matrix[self.pos(x_end, y_end)].is_finish = True

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
            if (self.matrix[self.pos(i,j)].isOrigin() == True):
              pixels[i,j] = (194, 231, 193)
            if (self.matrix[self.pos(i,j)].isFinish() == True):
              pixels[i,j] = (228, 151, 149 )
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

