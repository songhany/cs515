class Queue:
    def __init__(self):
         # TODO: Initialize the Queue
        self.storage = []
    
    def size(self):
         # TODO: Check the size of the Queue
        return len(self.storage)

    def enqueue(self, item):
         # TODO: Enter item into Queue
        self.storage.append(item)
            
    def dequeue(self):
         # TODO: Remove item from the Queue
        return self.storage.pop(0)