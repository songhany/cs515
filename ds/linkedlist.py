
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def print_linked_list(head):
    cur= head
    
    while cur is not None:
        print(cur.value)
        cur = cur.next
        
# print_linked_list(head)


def create_linked_list(input_list):   # O(n^2) which is very bad
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)    
        else:
        # Move to the tail (the last node)
            cur = head
            while cur.next:
                cur = cur.next
        
            cur.next = Node(value)
    return head


def create_linked_list_better(input_list):
    head = None
    tail = None
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    
    return head


def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
        return

    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode

LinkedList.prepend = prepend  # This is the way to add a function to a class after it has been defined


def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here 
    if self.head == None:
        self.head = Node(value)
        return
    
    cur = self.head
    while cur.next != None:
        cur = cur.next
    cur.next = Node(value)

LinkedList.append = append


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    if self.head == None:
        return None

    cur = self.head
    while cur != None:
        if cur.value == value:
            return cur
        cur = cur.next
    return None

LinkedList.search = search

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head == None:
        return
    
    firstNode = self.head
    self.head = self.head.next
    return firstNode.value
    
LinkedList.pop = pop


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here    
    if self.head == None:
        self.head = Node(value)
        return
    
    if pos == 0:
        self.prepend(value)
        return
    
    cur = self.head
    while pos > 1 and cur.next != None:
        cur = cur.next
        pos -= 1
        
    newNode = Node(value)
    newNode.next = cur.next
    cur.next = newNode
            
LinkedList.insert = insert


def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head == None:
        return
    if self.head.value == value:
        self.head = self.head.next
        return
    

    cur = self.head
    while cur.next != None:
        if cur.next.value == value:
            cur.next = cur.next.next
            return
            
        cur = cur.next

LinkedList.remove = remove


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here    
    if self.head == None:
        self.head = Node(value)
        return
    
    if pos == 0:
        self.prepend(value)
        return
    
    cur = self.head
    while pos > 1 and cur.next != None:
        cur = cur.next
        pos -= 1
        
    newNode = Node(value)
    newNode.next = cur.next
    cur.next = newNode
            
LinkedList.insert = insert
LinkedList.insert = insert

def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    size = 0
    cur = self.head
    while cur != None:
        cur = cur.next
        size += 1
    return size
        
LinkedList.size = size


if __name__ == "__main__":
    ### Test Code
    def test_function(input_list, head):
        try:
            if len(input_list) == 0:
                if head is not None:
                    print("Fail")
                    return
            for value in input_list:
                if head.value != value:
                    print("Fail")
                    return
                else:
                    head = head.next
            print("Pass")
        except Exception as e:
            print("Fail: "  + e)
        
    input_list = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(input_list)
    test_function(input_list, head)

    input_list = [1]
    head = create_linked_list(input_list)
    test_function(input_list, head)

    input_list = []
    head = create_linked_list(input_list)
    test_function(input_list, head)


    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

    # Test insert 
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"