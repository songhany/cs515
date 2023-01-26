import sys
import heapq
from collections import deque

class TreeNode(object):   

    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.left = None
        self.right = None
        self.bit = ''
        self.huffmanCode = None

    def getHuffmanCode(self, key):
        return self.huffmanCode

    def __lt__(self, other):   # https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
        return self.v < other.v


huffmanCodeMap = dict({})

def huffman_encoding(data):
    """ Phase I - Build the Huffman Tree """
    freq = dict({})
    for c in data:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    minheap = []
    for char, v in freq.items():
        newNode = TreeNode(char, v)
        heapq.heappush(minheap, newNode)

    while len(minheap) > 1:
        node1 = heapq.heappop(minheap)
        node2 = heapq.heappop(minheap)
        huffmanNewNode = TreeNode('', node1.v + node2.v)
        huffmanNewNode.left = node1
        huffmanNewNode.right = node2

        heapq.heappush(minheap, huffmanNewNode)

    # Until there is a single element left in the priority queue.
    # For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.
    root = minheap[0]
    levelOrderTraverseSetBit(root)

    """ Phase II - Generate the Encoded Data """
    generateEncodedData(root)

    encoded_data = ""
    for c in data:
        encoded_data += str(huffmanCodeMap[c])

    return encoded_data, root
    

def huffman_decoding(data, tree):
    decoded_data = ""
    curNode = tree
    for bit in data:
        # Start traversing the Huffman tree from the root
        if bit == '0':
            curNode = curNode.left
        elif bit == '1':
            curNode = curNode.right

        # If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
        if curNode.left == None and curNode.right == None:
            decoded_data += curNode.k
            curNode = tree

    return decoded_data


def levelOrderTraverseSetBit(root):
    queue = deque()
    queue.appendleft(root)

    while len(queue) != 0:
        curNode = queue.pop()

        if curNode.left != None:  # assign a bit 0 for left child 
            curNode.left.bit = '0'
            queue.appendleft(curNode.left)
        if curNode.right != None:  # assign a 1 for right child
            curNode.right.bit = '1'
            queue.appendleft(curNode.right)

def generateEncodedData(root):
    huffmanCode = ""
    preOrderTraverse(root, huffmanCode)
    
def preOrderTraverse(root, huffmanCode):
    if root == None:
        return

    huffmanCode += str(root.bit)
    preOrderTraverse(root.left, huffmanCode)
    preOrderTraverse(root.right, huffmanCode)

    if root.left == None and root.right == None:  # leaf node
        huffmanCodeMap[root.k] = huffmanCode
        root.huffmanCode = huffmanCode
        

if __name__ == "__main__":
    # codes = {}

    # a_great_sentence = "The bird is the word"

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
    encoded_data, tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
    print(encoded_data)  # 1010101010101000100100111111111111111000000010101010101
    print( int(encoded_data) == 1010101010101000100100111111111111111000000010101010101)  # True

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)  # AAAAAAABBBCCCCCCCDDEEEEEE
    print(decoded_data == "AAAAAAABBBCCCCCCCDDEEEEEE")  # True

# Test Case 2
    encoded_data, tree = huffman_encoding("The bird is the word")
    print(encoded_data)  # 1000111111100100001101110000101110110110100011111111001101010011100001

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)  # The bird is the word


# Test Case 3
    encoded_data, tree = huffman_encoding("I am Songhan Yu who I am")
    print(encoded_data)  # 110110010111110110000000111001011100100111100011011010110011110000101101100101111

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)  # I am Songhan Yu who I am


'''
(Unique) Character	Frequency	Huffman Code
        D	            2       	000
        B	            3       	001
        E	            6       	01
        A	            7	        10
        C	            7	        11

Points to Notice
1. Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a Prefix code.
2. Notice that the binary code is shorter for the more frequent character, and vice-versa.
3. The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
4. Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.
'''