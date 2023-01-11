## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()   # current.insert(char)
                
            current = current.children[char]
        
        current.is_word = True
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        if self.is_word:
            suffixes.append(suffix)
            
        for child in self.children:
            suffixes.extend(self.children[child].suffixes(suffix+child))
            
        return suffixes
    

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixNode = MyTrie.find('')
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))

# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact

# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
        
# interact(f,prefix='');