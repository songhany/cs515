import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calc_hash()
        self.previous_hash = previous_hash
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        if self.data != None:
            hash_str = self.data.encode('utf-8')
        else:
            hash_str = "None".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return f"Block(\nTimestamp: {self.timestamp},\n Data: {self.data},\n SHA256 Hash: {self.hash},\n Prev_Hash: {self.previous_hash }\n)\n"


class Blockchain:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, data):

        if self.head is None:
            self.head = Block(datetime.timestamp(datetime.now()), data, None)
            return

        preblock = None
        curblock = self.head
        while curblock != None:
            preblock = curblock
            curblock = curblock.next

        preblock.next = Block(datetime.timestamp(datetime.now()), data, preblock.hash)



# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
blockchain = Blockchain()
datalist = ["I am Songhan", "You are good", "All set"]
for data in datalist:
    blockchain.append(data)
print(blockchain)
'''
Block(
Timestamp: 1670882155.093491,
 Data: I am Songhan,
 SHA256 Hash: 6b824bfe0a981fad617e4959e81d094b2f44c550bea105f89cf6fbb815d4c1b6,
 Prev_Hash: None
)
 -> Block(
Timestamp: 1670882155.093501,
 Data: You are good,
 SHA256 Hash: afb30cb5ff0d7b3300dc3e245ed24ef244262f4409924f4888e66d0775edf54f,
 Prev_Hash: 6b824bfe0a981fad617e4959e81d094b2f44c550bea105f89cf6fbb815d4c1b6
)
 -> Block(
Timestamp: 1670882155.093503,
 Data: All set,
 SHA256 Hash: e3650cf206047955f04fce3c187cd4a82845c49e11bd10ef549978f5d923bdf5,
 Prev_Hash: afb30cb5ff0d7b3300dc3e245ed24ef244262f4409924f4888e66d0775edf54f
)
 -> 
'''

# Test Case 2
blockchain = Blockchain()
datalist = ["Bad Case", None, '']
for data in datalist:
    blockchain.append(data)
print(blockchain)
'''
Block(
Timestamp: 1670882155.09353,
 Data: Bad Case,
 SHA256 Hash: 94f6dbdbc298e32c6e34ba1533535b23c9e5b1d7bef09c8bdf16e11c797e8db0,
 Prev_Hash: None
)
 -> Block(
Timestamp: 1670882155.093533,
 Data: None,
 SHA256 Hash: dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91,
 Prev_Hash: 94f6dbdbc298e32c6e34ba1533535b23c9e5b1d7bef09c8bdf16e11c797e8db0
)
 -> Block(
Timestamp: 1670882155.093535,
 Data: ,
 SHA256 Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
 Prev_Hash: dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
)
 -> 
'''

# Test Case 3
blockchain = Blockchain()
datalist = ["", ""]
for data in datalist:
    blockchain.append(data)
print(blockchain)
'''
Block(
Timestamp: 1670882212.256556,
 Data: ,
 SHA256 Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
 Prev_Hash: None
)
 -> Block(
Timestamp: 1670882212.256578,
 Data: ,
 SHA256 Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,
 Prev_Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
)
 -> 
'''