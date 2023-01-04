import os
import queue

def find_files(suffix, path):
	"""
	Find all files beneath path with file name suffix.

	Note that a path may contain further subdirectories
	and those subdirectories may also contain further subdirectories.

	There are no limit to the depth of the subdirectories can be.

	Args:
		suffix(str): suffix if the file name to be found
		path(str): path of the file system

	Returns:
		a list of paths
	"""
	lstOfPath = []
	q = queue.Queue()
	q.put(path)
	while(q.qsize() > 0):
		curPath = q.get()
		lstdir = os.listdir(curPath)
		for dir in lstdir:
			if dir.endswith(suffix):
				lstOfPath.append(os.path.join(curPath, dir))
			else:
				nextPath = curPath + '/' + dir
				if os.path.isdir(nextPath):
					q.put(nextPath)
				
	return lstOfPath

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c", "testdir"))  # ['testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c']

# Test Case 2
print(find_files(".h", "testdir"))  # ['testdir/t1.h', 'testdir/subdir5/a.h', 'testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h']

# Test Case 3
print(find_files(".gitkeep", "testdir"))  # ['testdir/subdir4/.gitkeep', 'testdir/subdir2/.gitkeep']


'''
## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python
# Let us print the files in the directory in which you are running this script
print(os.listdir("./testdir"))
print(os.path.isdir("./testdir"))

# Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))
'''