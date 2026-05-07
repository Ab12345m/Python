from queue import PriorityQueue

# Graph as adjacency list with cost
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Heuristic values (h(n))
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))   # (f(n), node)

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {start: None}

    while not pq.empty():
        f, current = pq.get()

        # Goal check
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path:", path)
            print("Cost:", g_cost[goal])
            return

        # Explore neighbors
        for neighbor, cost in graph[current].items():
            new_g = g_cost[current] + cost

            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                pq.put((f_cost, neighbor))
                parent[neighbor] = current

    print("Goal not found!")

# Call function
a_star('A', 'F')