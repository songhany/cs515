class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""
def swap_nodes(head, lIdx, rIdx):
    # If both the indices are same
    if lIdx == rIdx:
        return head

    onePre = None
    oneCur = None
    
    twoPre = None
    twoCur = None
    
    cur = head
    curIdx = 0
    newHead = None
    
    # LOOP - find out previous and current node at both the positions (indices)
    while cur != None:
        if curIdx == lIdx:
            oneCur = cur
        elif curIdx == rIdx:
            twoCur = cur
            break
        
        # If neither of the leftIdx or rightIdx are equal to the curIndex
        if oneCur is None:
            onePre = cur

        twoPre = cur

        # increment both the currentIndex and currentNode
        cur = cur.next
        curIdx += 1
        
        
    '''SWAPPING LOGIC'''
    # We have identified the two nodes: oneCurrent & twoCurrent to be swapped, 
    # Make use of a temporary reference to swap the references
    twoPre.next = oneCur
    tmp = oneCur.next
    oneCur.next = twoCur.next
    twoCur.next = tmp
    
    # if the node at first index is head of the original linked list
    if onePre == None:
        newHead = twoCur
    else:
        onePre.next = twoCur
        newHead = head
    # Swapping logic ends

    return newHead
    