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
    self.h_size = h_size
    self.v_size = v_size
    self.matrix = []
    for i in range(v_size):
      for j in range(h_size):
        cell = Cell(j,i)
        self.matrix.append(cell)

  def pos(self, i, j):
    return i * self.v_size + j


test = Map(10,15)

test.matrix[test.pos(0,0)].is_obstacle = True
test.matrix[test.pos(0,1)].is_obstacle = True
test.matrix[test.pos(2,2)].is_obstacle = True
test.matrix[test.pos(5,7)].is_obstacle = True
test.matrix[test.pos(9,14)].is_obstacle = True

# # Create new black image of entire board
img = Image.new("RGB", (test.h_size, test.v_size))
pixels = img.load()

# Make pixels white where (row+col) is odd
for i in range(test.h_size):
    for j in range(test.v_size):
        if test.matrix[test.pos(i,j)].isObstacle() == False:
            pixels[i,j] = (255,255,255)

img = img.resize((50*test.h_size,50*test.v_size), Image.NEAREST)

img.show()
