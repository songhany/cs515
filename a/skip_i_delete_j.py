# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skip_i_delete_j_mySolution(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    if i == 0:    # Edge case - Skip 0 nodes (means Delete all nodes)
        return None

    if j == 0:
        return head

    if head == None or i < 0 or j < 0:   # Invalid input
        return head

    cntSkip = 0
    cntDel = 0
    cur = head
    while cur != None:
        while cur != None and cntSkip < i - 1:
            cur = cur.next
            cntSkip += 1
        
        if cur == None:
            return head

        
        nxt = cur
        while nxt != None and cntDel < j:
            nxt = nxt.next
            cntDel += 1
        
        if nxt == None:
            cur.next = None
        else:
            cur.next = nxt.next
            cur = cur.next
    
        cntSkip = 0
        cntDel = 0

    return head


# Solution
"""
:param: head - head of linked list
:param: i - first `i` nodes that are to be skipped
:param: j - next `j` nodes that are to be deleted
return - return the updated head of the linked list
"""
'''
The Idea: 
Traverse the Linkedist. Make use of two references - `current` and `previous`.
 - Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
 - Delete next `j` nodes. Keep incrementing the `current`.
 - Connect the `previous.next` to the `current`
'''
def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None
    
    # Edge case - Delete 0 nodes
    if j == 0:
        return head
    
    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    current = head
    previous = None
    
    # Traverse - Loop untill there are Nodes available in the LinkedList
    while current:
        
        '''skip (i - 1) nodes'''
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        '''delete next j nodes'''
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        
        '''Connect the `previous.next` to the `current`''' 
        previous.next = current
    
    return head


if __name__ == "__main__":
    def create_linked_list(arr):
        if len(arr)==0:
            return None
        head = Node(arr[0])
        tail = head
        for data in arr[1:]:
            tail.next = Node(data)
            tail = tail.next
        return head

    def print_linked_list(head):
        while head:
            print(head.data, end=' ')
            head = head.next
        print()


    linkedList1 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    solution = [1, 2, 5, 6, 9, 10]
    skip_i_delete_j(linkedList1, 2, 2)
    print_linked_list(linkedList1)

    linkedList2 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    solution = [1, 2, 6, 7, 11, 12]
    skip_i_delete_j(linkedList2, 2, 3)
    print_linked_list(linkedList2)

    linkedList3 = create_linked_list([1, 2, 3, 4, 5])  
    solution = [1, 2]
    skip_i_delete_j(linkedList3, 2, 4)
    print_linked_list(linkedList3)

    linkedList4 = create_linked_list([1, 2, 3, 4, 5])
    solution = [1, 2, 3, 4, 5]
    skip_i_delete_j(linkedList4, 2, 0)
    print_linked_list(linkedList4)
