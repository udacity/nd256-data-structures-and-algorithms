"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

duration = dict()

for i in calls:
    
    if (i[0] not in duration):
        duration[i[0]] = int(i[3])
    else:
        duration[i[0]] = int(i[3])+duration[i[0]]
    
    if (i[1] not in duration):
        duration[i[1]] = int(i[3])
    else:
        duration[i[1]] = int(i[3])  +duration[i[1]]


max = 0
phone_max = None
for phone, time in duration.items():
    if max <time:
        phone_max=phone
        max =time

print(f"{phone_max} spent the longest time, {max} seconds, on the phone during September 2016.")




