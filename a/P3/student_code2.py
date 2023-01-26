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


def heuristic(M, node, goalNode):  # node: intersection  goalNode: intersection   type(intersection) == int
    x1, y1 = M.intersections[node]
    x2, y2 = M.intersections[goalNode]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5   # calculate distance between Node and GoalNode. We can use it to calculate 'g' and 'h'


def shortest_path(M, start, goal):  # start: intersection  goal: intersection     type(intersection) == int
    startNode = GraphNode(start, 0, 0, 0)
    open = [startNode]    # minHeap
    close = []            # minHeap
    visited = set()       # Set store the visited nodes

    cost = {startNode: 0}     # Create a Map to store the cost of reaching each node
    pre = {startNode: None}   # Create a Map to store the previous node in the path as value  for each key node

    while len(open) != 0:
        curNode = heapq.heappop(open)   # curNode is instance of GraphNode instance
        visited.add(curNode)            # Mark the current node as visited

        if curNode.intersection == goal:
            path = []

            cur = curNode
            while cur != startNode:
                path.append(cur.intersection)
                cur = pre[cur]
            path.append(start)
            return path[::-1]

        # Get the neighbors of the current node
        for neighbor in M.roads[curNode.intersection]:
            if neighbor == goal:   # type(neighbor) == int. if neighbor is the goal, stop search
                pre[neighbor] = curNode
                path = []

                cur = neighbor
                while cur != start:
                    path.append(cur)
                    cur = pre[cur]
                path.append(start)
                return path[::-1]

            else:
                # compute both g and h for neighbor
                neighborNode = GraphNode(neighbor, 0, 0, 0)
                neighborNode.g = curNode.g + heuristic(M, curNode.intersection, neighbor)
                neighborNode.h = heuristic(M, neighborNode.intersection, goal)
                neighborNode.f = neighborNode.g + neighborNode.h

                if neighborNode in visited:
                    continue

                if neighborNode not in open:
                    heapq.heappush(open, neighborNode)  # generate neighborNode to the minHeap PriorityQueue with f(x) = g(x) + h(x). I encapsulate f(x) as property of GraphNode
                    pre[neighbor] = curNode.intersection
                    cost[neighbor] = neighborNode.f
                else:
                    if neighborNode.f < cost[neighbor]:
                        pre[neighbor] = curNode.intersection
                        cost[neighbor] = neighborNode.f
                        open.remove(neighborNode)
                        heapq.heappush(open, neighborNode)
    return None  # if no path found
                