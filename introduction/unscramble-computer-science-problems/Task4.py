"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

phone = set()

#add phone to set that make calls
for i in calls:
    if i[0][0:3] != '140':
        phone.add(i[0])

#remove phones that received incoming call
for i in calls:
    phone.discard(i[1])


#remove phones that received texts
for i in texts:
    phone.discard(i[0])
    phone.discard(i[1])

print("These numbers could be telemarketers: ")
print(*sorted(phone),sep='\n')