# Tucker - Applied Combinatorics 6e - Section 2.1 Ex. 20. (a)
# Given list of tuples representing edges, find Euler cycle
# if one exists. Output in form of list with elements representing
# consecutive vertices in Euler cycle. Output error if no Euler
# cycle exists.

def find_euler_cycle(G: list[tuple]):
    degree = {}

    # Check degree of all vertices, if not even, no Euler cycle exists
    for edge in G:
        if edge[0] not in degree.keys():
            degree[edge[0]] = 1
        else:
            degree[edge[0]] += 1
        if edge[1] not in degree.keys():
            degree[edge[1]] = 1
        else:
            degree[edge[1]] += 1
    if any(value % 2 != 0 for value in degree.values()):
        print("The graph G has no Euler cycle.")
    else:   # Find cycle and add to list
        cycle = []
        vertex = G[0][0]
        

