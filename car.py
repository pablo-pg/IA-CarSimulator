# Simulador del grupo 10
# Miembros: 
#     Helena García Díaz (alu0100829150@ull.edu.es)  
#     Javier Yoendy Hernández Martín (alu0101184753@ull.edu.es)  
#     Pablo Pérez González (alu0101318318@ull.edu.es)
#
# Clase Car. Se ocupará de todo el algoritmo y lo referido al movimiento del vehiculo.
from cell import Cell
from map import Map
from node import Node
import time
from PIL import Image

# Funcion 1 = Manhatan
# Funcion 2 = Euclidea

class Car:
  def __init__(self, map, number_directions = 4, function = 1): #, x_origin, y_origin, maps):
    #self.x_pos = x_origin
    #self.y_pos = y_origin
    #maps = maps
    self.number_directions = number_directions
    if (number_directions == 4):
      self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    if (number_directions == 8):
      self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    self.function = function
    self.map = map

  # Algoritmo A*
  def astar(self, map):
    node_explored = 0
    start = Cell(map.x_origin, map.y_origin, False, True, False)
    end = Cell(map.x_end, map.y_end, False, False, True)

    start_node = Node(start, None)
    start_node.G = start_node.H = start_node.F = 0
    end_node = Node(end, None)
    end_node.G = end_node.H = end_node.F = 0
    
    open_list = []
    closed_list = []

    open_list.append(start_node)
    node_explored += 1
    #print("Star node: ", start_node.cell.x_pos, start_node.cell.y_pos)

    while len(open_list) > 0:
      #print("NUEVA ITERACIÓN")
      #print("Tamaño open_list: ", len(open_list))
      current_node = open_list[0]
      current_index = 0
      for index, item in enumerate(open_list):
        if item.F < current_node.F:
          current_node = item
          current_index = index
      
      # Se saca de la lista abierta y se pasa a la cerrada
      open_list.pop(current_index)
      closed_list.append(current_node)
      
      # Se mira si ha llegado al final
      if current_node.cell.x_pos == end_node.cell.x_pos and current_node.cell.y_pos == end_node.cell.y_pos:
        path = []
        current = current_node
        while current is not None:
          path.append((current.cell.x_pos, current.cell.y_pos))
          current = current.parent
        print(f"{node_explored} nodos explorados")
        return path[::-1] # Se devuelve el camino ordenado

      # Se generan los hijos
      children = []
      # new_node = Node(start_node.cell)
      for new_position in self.directions: # Adjacent squares
        #print("\tNew_position: ", new_position[0], new_position[1])
        #print("\tCurrent node: ", current_node.cell.x_pos, current_node.cell.y_pos)
        # Calcular el siguiente candidato (de paso)
        node_position = (current_node.cell.x_pos + new_position[0], current_node.cell.y_pos + new_position[1])
        #print("\tPosicion nueva en mapa: ", node_position)

        # Comprobamos que no se sale del mapa
        #print("Primero: ", node_position[0] <= (map.h_size - 1))
        #print("Segundo: ", node_position[0] >= 0)
        #print("Tercero: ", node_position[1] <= (map.v_size -1))
        #print("Cuarto: ", node_position[1] >= 0)
        if node_position[0] <= (map.h_size - 1) and node_position[0] >= 0 and node_position[1] <= (map.v_size -1) and node_position[1] >= 0:
          #print("\t\tNode_position(81): ", node_position)
          # Se mira si no es un obstáculo
          #print ("\t\tObstaculo: ", map.matrix[map.pos(node_position[0], node_position[1])].isObstacle())
          if map.matrix[map.pos(node_position[0], node_position[1])].isObstacle() == False:  # False si no es un obstaculo     
            #print("\tNo es obstaculo")
            new_cell = Cell(node_position[0], node_position[1])
            new_node = Node(new_cell, current_node)
            children.append(new_node)
            #print(f"\tCandidato encontrado -> #{node_position}")
            # continue

        # Create new node
        # new_node = Node(current_node.cell, node_position)

        # Append
        # children.append(new_node)
      #if len(children) > 0:
        #print(f"Nodo guardado -> #{children[-1].id}")
      for child in children:
        # Child is on the closed list
        for closed_child in closed_list:
          if child == closed_child:
            #print("El nodo está en la lista cerrada")
            continue
          # else: print("DEBE PARAR")

        # Create the f, g, and h values
        child.G = current_node.G + Cell.move_cost
        if self.function == 1: # Manhatan
          child.H = child.cell.manhattanDistance(end.x_pos, end.y_pos)
        elif self.function == 2: # Euclidea
          child.H = child.cell.euclideanDistance(end.x_pos, end.y_pos)
        child.F = child.G + child.H
        #print(f"El valor de F es de {child.F}")
        # Child is already in the open list
        for open_node in open_list:
          if child == open_node and child.G > open_node.G:
            continue

        # Expandimos el arbol (Añadimos el hijo a la lista abierta)
        #print("Valores del child: ",child.cell.x_pos, child.cell.y_pos)
        open_list.append(child)
        node_explored += 1
      if child.F > 20:
        raise SystemExit

    # Hacer un throw por si no hay camino
    if len(closed_list) == 0:
      print("No hay camino")
      raise ValueError('No hay camino')
    else:
      print("Lista cerrada: ", closed_list)


  def algorithm(self, name):
    start_time = time.time()
    path = self.astar(self.map)
    ejecution_time = (time.time() -start_time)
    ejecution_time = format(ejecution_time, '.10E')
    print("Tiempo de ejecucion A*: ",ejecution_time)
    print("Path: ", path)
    self.print_whole(name, path)

  def print_whole(self, name, path):
    img = Image.new("RGB", (self.map.h_size, self.map.v_size))
    pixels = img.load()
    # Recorre todo el mapa y si no hay obstáculo lo pinta de blanco
    for i in range(self.map.h_size):
        for j in range(self.map.v_size):
            if self.map.matrix[self.map.pos(i,j)].isObstacle() == False:
                pixels[i,j] = (255,255,255)
            if self.map.matrix[self.map.pos(i,j)].isOrigin() == True:
              pixels[i,j] = (194, 231, 193)
            if self.map.matrix[self.map.pos(i,j)].isFinish() == True:
              pixels[i,j] = (228, 151, 149)
            for k in path:
              if self.map.matrix[self.map.pos(i,j)].x_pos == k[0] and self.map.matrix[self.map.pos(i,j)].y_pos == k[1]:
                #print("k: ", k)
                #print("pos: ", self.map.matrix[self.map.pos(i,j)].x_pos, self.map.matrix[self.map.pos(i,j)].y_pos)
                pixels[j,i] = (87, 106, 213)
    # Amplía la imagen
    img = img.resize((50 * self.map.h_size, 50 * self.map.v_size), Image.NEAREST)
    img.save(f'{name}.jpg')
