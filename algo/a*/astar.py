import heapq   # This solution pass all test case


class GraphNode(object):   

    def __init__(self, intersection, f, g, h):
        self.i = intersection
        self.f = f   # f = g + h
        self.g = g   # `g` is the distance traveled from start node to the frontier
        self.h = h   # `h` is straight line distance from the frontier to the goal (heuristic)

    def __lt__(self, other):
        return self.f < other.f


def heuristic(M, node, goalNode):  # calculate distance between Node and GoalNode. We can use it to calculate 'g' and 'h'
    x1, y1 = M.intersections[node]
    x2, y2 = M.intersections[goalNode]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5   

def shortest_path(M, start, goal):  # start: intersection  goal: intersection 
    startNode = GraphNode(start, 0, 0, 0)
    minheap = [startNode]    # minHeap
        
    visited = set()       # Set store the visited nodes

    cost = {startNode.i: 0}     # Map to store the cost of reaching each node
    prev = {startNode.i: None}  # Map to store the previous node in the path as value  for each key node

    while len(minheap) != 0:
        curNode = heapq.heappop(minheap)   # curNode is instance of GraphNode instance
        visited.add(curNode.i)             # Mark the current node as visited

        # Get the neighbors of the current node
        for neighbor in M.roads[curNode.i]:
            if neighbor == goal:   # type(neighbor) == int. if neighbor is the goal
                prev[neighbor] = curNode.i
                path = []
                cur = neighbor
                while cur != start:
                    path.append(cur)
                    cur = prev[cur]
                path.append(start)
                path.reverse()
                return path 

            else:
                if neighbor in visited:
                    continue
                # calculate g, h, f for the neighbor node
                g = cost[curNode.i] + heuristic(M, curNode.i, neighbor)
                h = heuristic(M, neighbor, goal)
                f = g + h
                
                if neighbor not in cost or g < cost[neighbor]:
                    cost[neighbor] = g
                    prev[neighbor] = curNode.i
                    heapq.heappush(minheap, GraphNode(neighbor, f, g, h))



'''
This solution uses the A* search algorithm to find the shortest path between two intersections on a given map. 
The A* algorithm is a popular choice for pathfinding because it combines the strengths of two other algorithms: Dijkstra's algorithm, which guarantees finding the shortest path, and the Best-first search algorithm, which allows for efficient exploration of the search space.

The key idea behind the A* algorithm is to use a heuristic function, in this case heuristic(M, node, goalNode), to guide the search towards the goal. 
The heuristic function estimates the distance between the current node and the goal node, and is used to calculate the f-value of each node. 
The f-value is the total cost of reaching a node, which is the sum of the cost of reaching the node (g-value) and the estimated cost of reaching the goal from the node (h-value).

In this solution, the heapq library is used to implement the min-heap data structure, which allows for efficient insertion and removal of nodes with the smallest f-value. 
The algorithm starts at the start node and explores its neighbors. 
If a neighbor is the goal node, the algorithm stops and returns the path. If a neighbor has already been visited, the algorithm skips it. 
Otherwise, the algorithm updates the cost and previous node of the neighbor, and adds it to the min-heap.

The algorithm continues this process until the min-heap is empty, at which point the goal node has not been reached and there is no path from start to goal.

Overall, this solution is an efficient way to find the shortest path between two points using the A* algorithm.

'''