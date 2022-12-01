"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
hashMap = {}

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # Task2   O(n)
    for call in calls:       
        callNum = call[0]
        recNum = call[1]
        duration = int(call[3])

        if callNum not in hashMap:
            hashMap[callNum] = duration
        else:
            hashMap[callNum] += duration

        if recNum not in hashMap:
            hashMap[recNum] = duration
        else:
            hashMap[recNum] += duration


    maxTime = 0
    maxTelephone = None
    for key, val in hashMap.items():
        if val > maxTime:
            maxTime = val
            maxTelephone = key
    
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxTelephone, maxTime))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

