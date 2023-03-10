import copy                                           # `copy` module

list1 = [0, 1, 2]
list2 = [7, 8, 9]                                     
compoundList1 = [list1, list2]                        # create a compound object


'''ASSIGNMENT OPERATION - Points a new reference to the existing object.'''
compoundList2 = compoundList1

# id() - returns the identity of the object passed
print(id(compoundList1) == id(compoundList2))          # True - compoundList2 is the same object as compoundList1
print(id(compoundList1[0]) == id(compoundList2[0]))    # True - compoundList2[0] is the same object as compoundList1[0]


'''SHALLOW COPY'''
compoundList2 = copy.copy(compoundList1)

print(id(compoundList1) == id(compoundList2))          # False - compoundList2 is now a new object
print(id(compoundList1[0]) == id(compoundList2[0]))    # True - compoundList2[0] is the same object as compoundList1[0]


'''DEEP COPY'''
compoundList2 = copy.deepcopy(compoundList1)

print(id(compoundList1) == id(compoundList2))          # False - compoundList2 is now a new object
print(id(compoundList1[0]) == id(compoundList2[0]))    # False - compoundList2[0] is now a new object