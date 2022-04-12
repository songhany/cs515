
def linearSearch(lst, key):
    for i in range(len(lst)):
      if lst[i] == key:
        return i
    return -1