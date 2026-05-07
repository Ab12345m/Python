# AO* Algorithm Implementation

# Graph representation (AND-OR graph)
# Format: node: [ (cost, [child nodes]) ]
graph = {
    'A': [(1, ['B', 'C']), (3, ['D'])],   # A → (B AND C) OR (D)
    'B': [(1, ['E']), (1, ['F'])],        # B → E OR F
    'C': [(1, ['G'])],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 1,
    'G': 0
}

# To store final solution path
solution = {}

def ao_star(node):
    # If node is terminal
    if node not in graph or len(graph[node]) == 0:
        return heuristic[node]

    min_cost = float('inf')
    best_children = None

    # Evaluate all possible AND-OR paths
    for cost, children in graph[node]:
        total_cost = cost

        # For AND nodes → sum of all children
        for child in children:
            total_cost += ao_star(child)

        # Select minimum cost option
        if total_cost < min_cost:
            min_cost = total_cost
            best_children = children

    # Update heuristic
    heuristic[node] = min_cost
    solution[node] = best_children

    return min_cost

def print_solution(node):
    print(node, end=" ")
    if node in solution:
        for child in solution[node]:
            print_solution(child)

# Run AO* Algorithm
start = 'A'
ao_star(start)

print("Solution Path:")
print_solution(start)

print("\nMinimum Cost:", heuristic[start])