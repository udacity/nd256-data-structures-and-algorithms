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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


#first record of tests
line = texts[0]

last_line =calls[-1]

print (f"First record of texts, {line[0]} texts {line[1]} at time {line[2]}")
print(f"Last record of calls, {last_line[0]} calls {last_line[1]} at time {last_line[2]}, lasting {last_line[3]} seconds")