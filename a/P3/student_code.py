import heapq

#  f, as defined by: f = g + h , 
# `g` is the distance traveled from start node to the frontier
# `h` is straight line distance from the frontier to the goal (heuristic)

class GraphNode(object):   

    def __init__(self, intersection, f, g, h):
        self.intersection = intersection
        self.f = f
        self.g = g
        self.h = h
        # self.roads = None

    def __lt__(self, other):   # https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
        return self.f < other.f


def heuristic(M, node, goalNode):
    x1, y1 = M.intersections[node]
    x2, y2 = M.intersections[goalNode]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5   # calculate distance between Node and GoalNode. We can use it to calculate 'g' and 'h'


def shortest_path(M, start, goal):  # start: intersection  goal: intersection 
    startNode = GraphNode(start, 0, 0, 0)
    open = [startNode]    # minHeap
    close = []            # minHeap
    visited = set()       # Set store the visited nodes

    cost = {startNode: 0}     # Create a Map to store the cost of reaching each node
    prev = {startNode: None}  # Create a Map to store the previous node in the path as value  for each key node

    while len(open) != 0:
        curNode = heapq.heappop(open)   # curNode is instance of GraphNode instance
        visited.add(curNode)            # Mark the current node as visited

        # Get the neighbors of the current node
        for neighbor in M.roads[curNode.intersection]:
            if neighbor == goal:   # type(neighbor) == int. if neighbor is the goal, stop search
                break

            else:
                # compute both g and h for neighbor
                neighborNode = GraphNode(neighbor, 0, 0, 0)
                neighborNode.g = curNode.g + neighborNode.g
                neighborNode.h = heuristic(M, neighborNode.intersection, goal)
                neighborNode.f = neighborNode.g + neighborNode.h

            heapq.heappush(open, neighborNode)  # generate neighborNode to the minHeap PriorityQueue with f(x) = g(x) + h(x). I encapsulate f(x) as property of GraphNode


        