# Graph definition
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'D': [('G', 1)],
    'E': [('D', 6)],
    'G': []
}

# Heuristic function
def h(n):
    H = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return H[n]

# Function to get neighbors
def get_neighbors(v):
    return graph[v]

# A* Algorithm
def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()

    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = None

        # find node with lowest f(n)
        for v in open_set:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v

        # if goal is reached
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return path

        # explore neighbors
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if m in g and g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist")
    return None


# Run the algorithm
aStarAlgo('A', 'G')
