#!/usr/local/bin/python3

import search

def printSolution(name, solution):
    print(
        "- Name: ", name ,
        "\n- Path: ", solution[0].path(), 
        "\n- Number of nodes visited: ", solution[1], 
        "\n- Number of nodes generated: ", solution[2],
        "\n----------------------"
    )

def printAllSolutions(problem):
    printSolution("Breadth First", search.breadth_first_graph_search(problem))
    printSolution("Depth First", search.depth_first_graph_search(problem))
    printSolution("Branch and bound", search.branch_and_bound_search(problem))
    printSolution("Branch and bound with subestimation", search.branch_and_bound_subestimation_search(problem))

def main():
    print("From A to B")
    printAllSolutions(search.GPSProblem('A', 'B', search.romania))
    print("From C to A")
    printAllSolutions(search.GPSProblem('C', 'A', search.romania))
    print("From D to O")
    printAllSolutions(search.GPSProblem('D', 'O', search.romania))
    print("From U to E")
    printAllSolutions(search.GPSProblem('U', 'E', search.romania))

if __name__ == "__main__":
    main()