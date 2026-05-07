# Minimax Algorithm Implementation

def minimax(depth, node_index, is_max, values, height):
    
    # Base case: leaf node reached
    if depth == height:
        return values[node_index]

    if is_max:
        # Maximizer's turn
        return max(
            minimax(depth + 1, node_index * 2, False, values, height),
            minimax(depth + 1, node_index * 2 + 1, False, values, height)
        )
    else:
        # Minimizer's turn
        return min(
            minimax(depth + 1, node_index * 2, True, values, height),
            minimax(depth + 1, node_index * 2 + 1, True, values, height)
        )

# Driver Code
values = [3, 5, 2, 9, 12, 5, 23, 23]   # Leaf node values
n = len(values)

# Calculate tree height
import math
height = int(math.log2(n))

# Run Minimax
result = minimax(0, 0, True, values, height)

print("Optimal Value:", result)