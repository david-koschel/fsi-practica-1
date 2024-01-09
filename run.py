# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

if __name__ == '__main__':
    print("Ruta: ", search.breadth_first_graph_search(ab).path())
    print("Ruta: ", search.depth_first_graph_search(ab).path())
    print("Ruta: ", search.branch_and_bound_graph_search(ab).path())
    print("Ruta: ", search.branch_and_bound_subestimation_graph_search(ab).path())

