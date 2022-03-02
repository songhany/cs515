#TAIL Recursion Exercise

#Write a tail resursive function that given a list as an input,
#returns the reverse of the list.

def reverseList(lst, a = []):
    if lst == []:
        return a
    return reverseList(lst[1:], [lst[0]] + a)

def test():
    assert reverseList([1,2,3]) == [3,2,1]
    assert reverseList([]) == []
    assert reverseList(["abc", "cde"]) == ["cde", "abc"]

test()