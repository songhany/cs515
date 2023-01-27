import heapq   # This solution only pass 2/3 test code.


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

    cost = {startNode: 0}     # Map to store the cost of reaching each node
    prev = {startNode: None}  # Map to store the previous node in the path as value  for each key node

    while len(minheap) != 0:
        curNode = heapq.heappop(minheap)   # curNode is instance of GraphNode instance
        visited.add(curNode.i)            # Mark the current node as visited

        # Get the neighbors of the current node
        for neighbor in M.roads[curNode.i]:
            if neighbor == goal:   # if neighbor is the goal, we find one of the path and record path. But it is may not optimal
                prev[neighbor] = curNode.i
                path = []
                curNode = neighbor
                while curNode != start:
                    path.append(curNode)
                    curNode = prev[curNode]
                path.append(start)
                return path[::-1]

            else:
                # compute both g and h for neighbor
                neighborNode = GraphNode(neighbor, 0, curNode.g + heuristic(M, curNode.i, neighbor), heuristic(M, neighbor, goal))
                if neighbor in visited:
                    continue
                if neighbor not in cost or neighborNode.f < cost[neighbor]:
                    cost[neighbor] = neighborNode.f
                    prev[neighbor] = curNode.i
                    heapq.heappush(minheap, neighborNode)
    return None # if goal not reached 
