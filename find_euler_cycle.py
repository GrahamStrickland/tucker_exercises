# Tucker - Applied Combinatorics 6e - Section 2.1 Ex. 20. (a)
# Given list of tuples representing edges, find Euler cycle
# if one exists. Output in form of list with elements representing
# consecutive vertices in Euler cycle. Return empty list if no Euler
# cycle exists.

def find_euler_cycle(V: list[int], E: list[tuple]):
    """Return a list containing an Euler cycle in the graph represented 
    by G = (V, E) if one exists, otherwise return empty list."""
    degrees = {vertex: 0 for vertex in V}

    # Add all degrees
    for edge in E:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    # Check degree of all vertices, if not even, no Euler cycle exists
    if any(value % 2 != 0 for value in degrees.values()):
        return []
    else:   # Find Euler cycle
        e_cycle = []
        curr_edge = E[0]
        E.remove(curr_edge)
        e_cycle.append(curr_edge[0])
        e_cycle.append(curr_edge[1])
        while len(E) > 0:
            for edge in E:
                if curr_edge[1] in edge:
                    if curr_edge[1] == edge[0]:
                        e_cycle.append(curr_edge[0])
                        e_cycle.append(curr_edge[1])
                    else:
                        e_cycle.append(curr_edge[1])
                        e_cycle.append(curr_edge[0])
                    curr_edge = edge
                    E.remove(curr_edge)

        return e_cycle
