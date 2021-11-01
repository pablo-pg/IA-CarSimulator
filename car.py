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
    start = Cell(map.x_origin, map.y_origin, False, True, False)
    end = Cell(map.x_end, map.y_end, False, False, True)

    start_node = Node(start)
    start_node.G = start_node.H = start_node.F = 0
    end_node = Node(end)
    end_node.G = end_node.H = end_node.F = 0
    
    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
      current_node = open_list[0]
      current_index = 0
      for index, item in enumerate(open_list):
        if item.F < current_node.F:
          current_node = item
          current_index = index
      
      # Se saca de la lista abierta y se pasa a la cerrada
      open_list.pop(current_index)
      closed_list.append(current_node)
      
      # Se busca el camino
      if current_node == end_node:
        path = []
        current = current_node
        while current is not None:
          path.append(current.position)
          current = current.parent
        return path[::-1] # Return reversed path

      # Se generan los hijos
      children = []
      for new_position in self.directions: # Adjacent squares
        # Get node position
        # node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
        node_position = (current_node.cell.x_pos + new_position[0], current_node.cell.y_pos + new_position[1])

        # Make sure within range
        if node_position[0] > (map.v_size - 1) or node_position[0] < 0 or node_position[1] > (map.h_size -1) or node_position[1] < 0:
            continue

        # Make sure walkable terrain
        # if map[node_position[0]][node_position[1]] != 0:
        print ("Linea 78: ", node_position)
        if map.matrix[map.pos(node_position[0], node_position[1])].isObstacle() == True:  # False si no es un obstaculo
            continue

        # Create new node
        new_node = Node(current_node, node_position)

        # Append
        children.append(new_node)
      
      for child in children:
        # Child is on the closed list
        for closed_child in closed_list:
          if child == closed_child:
            continue

        # Create the f, g, and h values
        child.G = current_node.G + Cell.move_cost
        if self.function == 1: # Manhatan
          child.H = child.ManhattanDistance(end.x_pos, end.y_pos)
        elif self.function == 2: # Euclidea
          child.H = child.cell.euclideanDistance(end.x_pos, end.y_pos)
        child.f = child.g + child.h

        # Child is already in the open list
        for open_node in open_list:
          if child == open_node and child.g > open_node.g:
            continue

        # Expandimos el arbol (Añadimos el hijo a la lista abierta)
        open_list.append(child)     
      
    # Hacer un throw por si no hay camino
    if len(closed_list) == 0:
      print("No hay camino")
      raise ValueError('No hay camino')
    else:
      print("Lista cerrada: ", closed_list)

    # Controlar los límites del mapa
    # Ver que la casilla no está ocupada por un obstáculo

    # Movimiento en función del caso

  def algorithm(self):
    start_time = time.time()
    path = self.astar(self.map)
    ejecution_time = (time.time() -start_time)
    ejecution_time = format(ejecution_time, '.10E')
    print("Tiempo de ejecucion A*: ",ejecution_time)
    print("Path: ", path)
