class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    hashset = set()
    cur1 = llist_1.head
    cur2 = llist_2.head
    while cur1 != None:
        hashset.add(cur1.value)
        cur1 = cur1.next

    while cur2 != None:
        hashset.add(cur2.value)
        cur2 = cur2.next

    newLinkedList = LinkedList()
    for val in hashset:
        newLinkedList.append(val)

    return newLinkedList


def intersection(llist_1, llist_2):
    # Your Solution Here
    hashset = set()

    cur1 = llist_1.head
    while cur1 != None:
        cur2 = llist_2.head
        while cur2 != None:
            if cur1.value == cur2.value:
                hashset.add(cur1.value)
                break
            cur2 = cur2.next
        cur1 = cur1.next

    newllt = LinkedList()
    for val in hashset:
        newllt.append(val)

    return newllt

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))  # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2))  # 4 -> 21 -> 6 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))  # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print (intersection(linked_list_3,linked_list_4))  # 

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, float('-inf'), None, float('inf'), pow(2, 64)]
element_2 = [9, float('inf'), None ]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))  # 1 -> None -> 18446744073709551616 -> 9 -> inf -> -inf -> 
print (intersection(linked_list_1,linked_list_2))  # None -> inf -> 

# Test Case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, None, None, None, None, 3]
element_2 = [1, 3, None, None]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))         # 1 -> 3 -> None ->
print (intersection(linked_list_1,linked_list_2))  # 1 -> 3 -> None ->


# Test Case 3

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3,4,5,6,7,8,9]
element_2 = [9,8,7,6,5,4,3,2,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))         # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 
print (intersection(linked_list_1,linked_list_2))  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 