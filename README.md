# Path finder

## Programming exercise that finds a paths from a node to another using informed/uninformed search

Para el ejercicio, se han creado dos clases nuevas: `BandBQueue` para ramificación y acotación y `BandBSubQueue` para ramificación y acotación con subestimación.

Ambas clases heredan de la clase `FIFOQueue`, ya que en su definición, son lo mismo: Colas en las que primer ítem de la lista es el primero que sale. La diferencia principal, es que cada vez que se insertan elementos a la lista, se modifica el orden de la lista en base a un criterio.

Al hacer uso de la función `extend(self, items)` de la clase `BandBQueue`, después de insertarse los elementos, se reordena a partir del coste del camino desde el nodo inicial hasta dicho inicio.

Por otra parte, al hacer uso de la función `extend(self, items)` de la clase `BandBSubQueue`, después de insertarse los elementos, se reordena a partir de la suma coste del camino desde el nodo inicial hasta dicho inicio junto con un valor heurístico obtenido con la función `h(node)` del objeto `GPSProblem`: la distancia entre el nodo origen y el destino.

Finalmente, se ha creado dos funciones, `branch_and_bound_search(problem)` y `branch_and_bound_subestimation_search(problem)`, que devuelven una solución al problema pasado por parámetro usando un objeto de las respectivas clases que hemos creado.

Salidas:

- From A to B
```
- Name:  Breadth First 
- Path:  [<Node B>, <Node F>, <Node S>, <Node A>] 
- Number of nodes visited:  16 
- Number of nodes generated:  21 
----------------------
- Name:  Depth First 
- Path:  [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] 
- Number of nodes visited:  10 
- Number of nodes generated:  18 
----------------------
- Name:  Branch and bound 
- Path:  [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] 
- Number of nodes visited:  24 
- Number of nodes generated:  31 
----------------------
- Name:  Branch and bound with subestimation 
- Path:  [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] 
- Number of nodes visited:  6 
- Number of nodes generated:  16 
----------------------
```

- From C to A
```
- Name:  Breadth First 
- Path:  [<Node A>, <Node S>, <Node R>, <Node C>] 
- Number of nodes visited:  15 
- Number of nodes generated:  24 
----------------------
- Name:  Depth First 
- Path:  [<Node A>, <Node Z>, <Node O>, <Node S>, <Node F>, <Node B>, <Node P>, <Node C>] 
- Number of nodes visited:  16 
- Number of nodes generated:  24 
----------------------
- Name:  Branch and bound 
- Path:  [<Node A>, <Node S>, <Node R>, <Node C>] 
- Number of nodes visited:  21 
- Number of nodes generated:  30 
----------------------
- Name:  Branch and bound with subestimation 
- Path:  [<Node A>, <Node S>, <Node R>, <Node C>] 
- Number of nodes visited:  6 
- Number of nodes generated:  15 
----------------------
```

- From D to O
```
- Name:  Breadth First 
- Path:  [<Node O>, <Node S>, <Node R>, <Node C>, <Node D>] 
- Number of nodes visited:  21 
- Number of nodes generated:  31 
----------------------
- Name:  Depth First 
- Path:  [<Node O>, <Node S>, <Node F>, <Node B>, <Node P>, <Node C>, <Node D>] 
- Number of nodes visited:  13 
- Number of nodes generated:  22 
----------------------
- Name:  Branch and bound 
- Path:  [<Node O>, <Node S>, <Node R>, <Node C>, <Node D>] 
- Number of nodes visited:  27 
- Number of nodes generated:  37 
----------------------
- Name:  Branch and bound with subestimation 
- Path:  [<Node O>, <Node S>, <Node R>, <Node C>, <Node D>] 
- Number of nodes visited:  12 
- Number of nodes generated:  24 
----------------------
```

- From U to E
```
- Name:  Breadth First 
- Path:  [<Node E>, <Node H>, <Node U>] 
- Number of nodes visited:  12 
- Number of nodes generated:  20 
----------------------
- Name:  Depth First 
- Path:  [<Node E>, <Node H>, <Node U>] 
- Number of nodes visited:  3 
- Number of nodes generated:  6 
----------------------
- Name:  Branch and bound 
- Path:  [<Node E>, <Node H>, <Node U>] 
- Number of nodes visited:  7 
- Number of nodes generated:  13 
----------------------
- Name:  Branch and bound with subestimation 
- Path:  [<Node E>, <Node H>, <Node U>] 
- Number of nodes visited:  3 
- Number of nodes generated:  6 
----------------------
```