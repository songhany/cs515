## problem_1.py
**why did you use that data structure?**  
I used Double LinkedList as data structure, because it will spend time O(1) to "add Node at Head" and time O(1) to "remove Node".
With Double LinkedList, it guarantee all operations must take O(1) time.

**Time efficiency and Space efficiency**  
Time  
get(self, key)         O(1)  
set(self, key, value)  O(1)  
remove(self, node)     O(1)  
addToHead(self, node)  O(1)  

Space O(n)
Because we create a HashMap as cache to store node. I don't conside LRU_Cache default capacity.


## problem_2.py
**why did you use that data structure?**   
I used Queue. Because we can regard file system path as N-ary Tree, here I use Breath First Search to find files. At the process of searching, I put sub_dir_path into Queue.

**Time efficiency and Space efficiency**  
Time O(n). Since the worst case is to iterate all sub_path under path.

Space O(n). Since I create a Queue for Breath First Search, in the worst case, I need store all sub_path of path into Queue once.


## problem_3.py
**why did you use that data structure?**  
Firstly, I used HashMap(i.e. freq) to calcuate frequency of each characters.  
Secondly, I used MinHeap, where a node that has lower frequency should have a higher priority to be popped-out.  
Then, I used second HashMap(i.e. huffmanCodeMap) to store Huffman Code for the corresponding character. 

**Time efficiency and Space efficiency**  
Time total O(nlogn)  
calcualte char frequency       O(n)  
minheap heappush() && heappop  O(nlogn)  
levelOrderTraverseSetBit()     O(n)  
generateEncodedData()          O(n)

Space O(n). Since I create a MinHeap and two HashMap.  


## problem_4.py
**why did you use that data structure?**  
I don't use data stucture in this problem.  

**Time efficiency and Space efficiency**  
Time O(n). Since I use is_user_in_group() in recursive way. The call stack is n level, i.e. there are n node in recusion tree.  

Space O(n). There are n level call stack at most, which is O(n) space.  


## problem_5.py
**why did you use that data structure?**  
I used Single LinkedList. Since a Blockchain is a sequential chain of records, similar to a linked list.

**Time efficiency and Space efficiency**  
Time  
calc_hash(self)     O(1) 
append(self, data)  O(n). Since using Single LinkedList, I have to use while loop to find final Block in Blockchain and then append new Block on blockchain.  
I think I can optimize this operation to time O(1). If I use Double LinkedList and add 'self.pre = None' property to Block.

Space O(1)
If I don't consider the space of Blockchain per se, I don't new extra data structure or create any new object. The space on stack and heap is O(1).


## problem_6.py
**why did you use that data structure?**  
I used hashset for eliminating duplicated element. Since the union of two sets A and B is the set. Same, The intersection of two sets A and B, denoted by A ∩ B, is the set.  

**Time efficiency and Space efficiency**  
Time  
union(llist_1, llist_2) O(n). Because I while loop both llist_1 and llist_2, then for lopp the hashset.

intersection(llist_1, llist_2) O(n^2). Because I use two nested while loop, the worst case is that there is no any intersection elemnet in llist_1 and llist_2.  

Space  
union(llist_1, llist_2) O(n). Because I create hashset to eliminate duplicated elements.  
intersection(llist_1, llist_2) O(n). Because I create hashset to elimininate duplicated elements.



