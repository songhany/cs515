# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

    
def reverse(linked_list):
    newList = LinkedList()
    pre = None
    for v in linked_list:
        newNode = Node(v)
        newNode.next = pre
        pre = newNode
        
    newList.head = pre
    return newList


# def reverse(linked_list):  # This cannot pass test, since after calling reverse(llist), the llist become [4]
#     newList = LinkedList()
#     head = linked_list.head
    
#     pre = None
#     while head != None:
#         nxt = head.next  # record head.nextNode
        
#         head.next = pre  # reverse curNode. This directly cause llist [4,2,5,1,-3,0] become [4]
        
#         pre = head   # move pointer
#         head = nxt
    
#     newList.head = pre
#     return newList


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
