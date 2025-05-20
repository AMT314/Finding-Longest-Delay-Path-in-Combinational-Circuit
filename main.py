from collections import defaultdict, deque

def longest_weighted_path(edges, primary_inputs, primary_outputs):
    """
    Finds and prints the longest weighted path from primary inputs to primary outputs in a directed graph.

    Parameters:
    edges: list of tuples representing directed edges with weights (from_node, to_node, weight)
    primary_inputs: list of nodes that are primary inputs
    primary_outputs: list of nodes that are primary outputs

    Returns:
    None - prints the longest weighted path and its length
    """
    # Build adjacency list and in-degrees
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()

    for from_node, to_node, weight in edges:
        adj_list[from_node].append((to_node, weight))
        in_degree[to_node] += 1
        nodes.add(from_node)
        nodes.add(to_node)

    # Initialize topological order using Kahn's algorithm
    queue = deque([node for node in nodes if in_degree[node] == 0])
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)
        for neighbor, _ in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Initialize distance and paths for dynamic programming
    distances = {node: float('-inf') for node in nodes}
    paths = {node: [] for node in nodes}

    # Primary inputs start with distance 0 and paths start from themselves
    for node in primary_inputs:
        distances[node] = 0
        paths[node] = [node]

    # Compute longest weighted path using topological order
    for node in topological_order:
        for neighbor, weight in adj_list[node]:
            if distances[node] + weight > distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                paths[neighbor] = paths[node] + [neighbor]

    # Find the longest weighted path among the primary outputs
    longest_path = []
    max_weight = float('-inf')

    for output in primary_outputs:
        if distances[output] > max_weight:
            max_weight = distances[output]
            longest_path = paths[output]

    # Print the longest weighted path and its length
    print("Longest Weighted Path from Primary Input to Output:")
    if longest_path:
        print(" -> ".join(map(str, longest_path)))
        print(f"Total Weight of the Path: {max_weight}")
    else:
        print("No path exists from primary inputs to primary outputs.")
