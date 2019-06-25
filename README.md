# Path finder

## Simple program that finds a path from a node to another using informed/uninformed search

Implementation of branch and bound without and with underestimation algorithms using two types of priority queue sorting criteria: distance for branch and bound, and distance plus an heuristic (euclidean distance to the objective).

Example outputs:

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
