"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

calls = None
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PartA   O(n) + O(klogk)  assume there is k telephone number in hashSet
hashSet = set()

for call in calls:
	callNum = call[0]
	recNum = call[1]

	if callNum.startswith("(080)"):  # call from Bangalore
		if recNum.startswith("("):   # fixed line numbers
			for idxClosePar in range(1, len(recNum)):
				if recNum[idxClosePar] == ")":
					hashSet.add(recNum[:idxClosePar + 1])
					break
		elif recNum.startswith("7") or recNum.startswith("8") or recNum.startswith("9"):  # Mobile numbers
			lst = recNum.split(" ")
			prefixMobileNum = lst[0][:4]
			hashSet.add(prefixMobileNum) 
		elif recNum.startswith("140"):  # telemarketers
			hashSet.add("140")

lst = sorted(list(hashSet))
print("The numbers called by people in Bangalore have codes:")
for teleNum in lst:
	print(teleNum)


# PartB   O(n)
totalCallFromBangalore = 0
callBetweenBangalore = 0
for call in calls:
	callNum = call[0]
	recNum = call[1]

	if callNum.startswith("(080)"):
		totalCallFromBangalore += 1
		if recNum.startswith("(080)"):
			callBetweenBangalore += 1

percent = callBetweenBangalore / totalCallFromBangalore * 100
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
