import heapq

def heuristic(M, node, goal):
    x1, y1 = M.intersections[node]
    x2, y2 = M.intersections[goal]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def shortest_path(M, start, goal):
    print("shortest path called")
    # Create a priority queue to store the next nodes to visit
    queue = [(0, start)]
    # Create a dictionary to store the cost of reaching each node
    cost = {start: 0}
    # Create a dictionary to store the previous node in the path for each node
    prev = {start: None}
    # Create a set to store the visited nodes
    visited = set()
    
    while queue:
        # Get the node with the lowest cost
        current_cost, current_node = heapq.heappop(queue)
        # If the current node is the goal, we're done
        if current_node == goal:
            break
        # If the current node has already been visited, skip it
        if current_node in visited:
            continue
#         # If the current_node is not in the M.roads return empty path
#         if current_node not in M.roads:
#             return []

        # Mark the current node as visited
        visited.add(current_node)
        # Get the neighbors of the current node
        for neighbor, edge_cost in M.roads[current_node]:
            # Calculate the cost of reaching the neighbor through the current node
            new_cost = current_cost + edge_cost
            # If the new cost is lower than the previously recorded cost for the neighbor
            if neighbor not in cost or new_cost < cost[neighbor]:
                # Update the cost and previous node for the neighbor
                cost[neighbor] = new_cost
                prev[neighbor] = current_node
                # Add the neighbor to the priority queue with the f(x) = g(x) + h(x)
                heapq.heappush(queue, (new_cost + heuristic(M, neighbor, goal), neighbor))
                
    # Create the final path by following the previous nodes from the goal
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = prev[node]
    # Return the path in reverse order
    return path[::-1]
