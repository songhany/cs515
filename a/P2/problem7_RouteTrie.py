# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
    
    def insert(self, path_part, handler=None):
        # Insert the node as before
        self.children[path_part] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path: list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curNode = self.root
        for path_part in path:
            if path_part not in curNode.children:  
                curNode.children[path_part] = RouteTrieNode()  # < key= path_part, val= RouteTrieNode() >
            curNode = curNode.children[path_part]

        # assign the handler to only the leaf (deepest) node of this path
        curNode.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curNode = self.root
        for path_part in path:
            if path_part not in curNode.children:
                return None
            curNode = curNode.children[path_part]
        return curNode.handler


''' The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.'''
class Router:
    def __init__(self, handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie()
        self.route_trie.insert(["/"], handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts as a list to the RouteTrie
        path_parts = self.split_path(path)   # path_parts is a List
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        if handler is None:  # response for 404 error "Page not found"
            return self.not_found_handler
        return handler

    def split_path(self, path: str):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == "/":
            return ['/']
        return path.strip("/").split("/")


# Here are some test cases and expected outputs you can use to test your implementation

# test case1
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))              # should print 'root handler'
print(router.lookup("/home"))          # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))    # should print 'about handler'
print(router.lookup("/home/about/"))   # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# test case2
print("===================================================")
router.add_handler("/root/src", "src")  # add a route
print(router.lookup("/root"))       # 'not found handler' 
print(router.lookup("/root/src"))   # 'src'
print(router.lookup("/root/src/"))  # 'src'
print(router.lookup("/root/m"))     # 'not found handler' 

# test case3
print("===================================================")
router.add_handler("/songhan", "personal")  # add a route
print(router.lookup("/songhan"))            # 'personal' 

# edge case1
print("===================================================")
router.add_handler("", "null")   # add a route
print(router.lookup("/"))        # "null"