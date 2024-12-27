# Graph definition
graph = {
    'S': [('A', 3), ('B', 2), ('X', 6)],
    'A': [('X', 1), ('C', 4)],
    'B': [('Y', 5)],
    'X': [('C', 2)],
    'C': [('Y', 1)],
    'Y': []
}

# Heuristic table (h-cost)
H_table = {
    'S': 7,
    'A': 4,
    'B': 6,
    'X': 2,
    'C': 1,
    'Y': 0  # Goal
}

# Function to calculate f-cost (g-cost + h-cost)
def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = g_cost + h_cost
    return f_cost, last_node

# A* Algorithm
def A_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]  # Start with the initial node
    while queue:
        # Sort paths by f-cost
        queue.sort(key=path_f_cost)
        # Take the path with the lowest f-cost
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            # Get adjacent nodes
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)
    return None  # If no path is found

# Interactive part
while True:
    print("\nAvailable Drugs: A, B, X, C, Y")
    goal_node = input("Enter the Drug you need ('A', 'B', 'X', 'C', 'Y'): ").strip()

    if goal_node not in graph:
        print("Invalid goal node. Please try again.")
        continue

    start_node = 'S'  # Fixed start node
    solution = A_star_search(graph, start_node, goal_node)
    if solution:
        print("\nSolution Path:", solution)
        print("Cost of Solution:", path_f_cost(solution)[0])
    else:
        print("No path found from", start_node, "to", goal_node)

    cont = input("\nDo you want to find another path? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("Exiting. Goodbye!")
        break
