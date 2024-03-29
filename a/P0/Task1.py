"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
hashset = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for t in texts:  
        hashset.add(t[0])
        hashset.add(t[1])  
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for c in calls:   # O(n)
        hashset.add(c[0])
        hashset.add(c[1])  
        
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Task1  O(n)
print("There are {} different telephone numbers in the records.".format(len(hashset)))