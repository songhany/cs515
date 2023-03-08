class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self, new_node):
        self.children.append(new_node)
    
    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list
        
    def add_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph1.nodes:
    print('parent node = ', each.value, end='\nchildren\n')
    for each in each.children:
        print(each.value, end=' ')
    print('\n')


#! Iterative dfs
def dfs_search(root_node, search_value):
    visited = set()                         # Sets are faster for lookups
    stack = [root_node]                     # Start with a given root node
    
    while len(stack) > 0:
        curNode = stack.pop()
        visited.add(curNode)
        
        if curNode.value == search_value:
            return curNode
        
        # Check all the neighbours of curNode
        for child in curNode.children:
            
            if (child not in visited) and (child not in stack):  # If a node hasn't been visited before, and not available in the stack already.
                stack.append(child)


# assert nodeA == dfs_search(nodeS, 'A')
# assert nodeS == dfs_search(nodeP, 'S')
# assert nodeR == dfs_search(nodeH, 'R')
# ======================================================================


#! Recursive dfs
def dfs_recursion_start(start_node, search_value):
    visited = set()               # Set to keep track of visited nodes.
    return dfs_recursion(start_node, visited, search_value)

# Recursive function
def dfs_recursion(node, visited, search_value):
    if node.value == search_value:
        found = True              # Don't search in other branches, if found = True
        return node
    
    visited.add(node)
    found = False
    result = None

    # Conditional recurse on each neighbour
    for child in node.children:
        if (child not in visited):
                result = dfs_recursion(child, visited, search_value)
                
                # Once the match is found, no more recurse 
                if found:
                    break
    return result


# assert nodeA == dfs_recursion_start(nodeG, 'A')
# assert nodeA == dfs_recursion_start(nodeS, 'A')
# assert nodeS == dfs_recursion_start(nodeP, 'S')
# assert nodeR == dfs_recursion_start(nodeH, 'R')
# ======================================================================


#! Iterative bfs
def bfs_search(root_node, search_value):
    visited = set()
    queue = [root_node]
    
    while len(queue) > 0:
        curNode = queue.pop(0)
        visited.add(curNode)
        if curNode.value == search_value:
            return curNode
        
        for child in curNode.children:
            if child not in visited:
                queue.append(child)


assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')