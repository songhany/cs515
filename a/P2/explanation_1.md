## problem_1.py
**why did you use that data structure?**  
Since it expected time complexity is O(log(n)), I use binary search to implement sqrt

**Time efficiency and Space efficiency**  
Time  O(logn)
Space O(1)


## problem_2.py
**why did you use that data structure?**   
Since it expected time complexity is O(log(n)), I use binary search

**Time efficiency and Space efficiency**  
Time O(logn). Since the worst case is to iterate all sub_path under path.
Space O(1)


## problem_3.py
**why did you use that data structure?**  
I used hashmap and arraylist data structure

**Time efficiency and Space efficiency**  
Time O(n * m).  There are three for loop traversal in this solution, since it traverses the input array, creates a dictionary in O(n) time. The `in` operation has linear time complexity O(m).

Space O(n).  Since I create a dictionary and two sorted array.  


## problem_4.py
**why did you use that data structure?**  
I don't use data stucture in this problem, but use 3 pointer to partition 0, 1, 2

**Time efficiency and Space efficiency**  
Time O(n).  It traverses the input array once

Space O(1). It swap in place with any auxilliary space


## problem_5.py
**why did you use that data structure?**  
Trie is good for autocomplete

**Time efficiency and Space efficiency**  
Time  
TrieNode
    insert(self, char)             O(1)
    suffixes(self, suffix = ''):   O(n)  Since I use recursive to iterate all possible suffixes result in recursion tree. And when suffixes is_word=True, I push suffixes into List to return.

Trie
    insert(self, word)   O(n)
    find(self, word)     O(n)

Space 
    suffixes(self, suffix = '')    O(n)
    all other function             O(1)



## problem_6.py
**why did you use that data structure?**  
no data structure, but just iterate the list of integers once.

**Time efficiency and Space efficiency**  
Time   O(n).  just iterate the list of integers once.
Space  O(1)



## problem_7.py
**why did you use that data structure?**  
Trie.

**Time efficiency and Space efficiency**  
Time

RouteTrieNode
    insert(self, path_part, handler=None)   O(1)

RouteTrie
   insert(self, path: list, handler)   O(n)
   find(self, path)                    O(n)

Router
    add_handler(self, path, handler)   O(n)
    lookup(self, path)        O(n)
    split_path(self, path)    O(n)

Space   O(n) depends number of RouteTrieNode