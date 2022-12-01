"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:  
    reader = csv.reader(f)
    texts = list(reader)

    fInNum = texts[0][0]
    fAnsNum = texts[0][1]
    fTime = texts[0][2]


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    lInNum = calls[-1][0]
    lAnsNum = calls[-1][1]
    lTime = calls[-1][2]
    lDuring = calls[-1][3]


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, {} texts {} at time {}".format(fInNum, fAnsNum, fTime))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(lInNum, lAnsNum, lTime, lDuring))
