## Task0
**Description**: The problem is to read two csv files and get the first record of record from one file and last records from the other file. These records are then printed.

**Approach**: identify the first record using index [0] and last line using index [-1] and then print the records.

**Complexity Analysis**:
- **Algorithm**: Access the first and last records using python index notation and then print the records.
- **Big O Notation**: $O(1)$ for access the records after CSV has been loaded.
- **Justification**: Each element is accessed by its index which is time constant.

## Task1
**Description**: The problem is to read two csv files and identify how many different phone numbers are present in the files.

**Approach**: loop over the records in both files. Create a set and add each phone numbers to this set. Since set stores unique values, its length give the total number of phone numbers.

**Complexity Analysis**:
- **Algorithm**: Loop over the records and add each phone number to the set. Use the length of the set to get unique phone numbers..
- **Big O Notation**: $O(n)$ where $n$ is the number of records.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the array size.


## Task2
**Description**: The problem is identifying which phone has spend maximum total time on phone.

**Approach**: Phone call records are in calls.csv file. Review the records of this file line by line. Create a dictionary and check if the phone number is already in the dictionary or not. Accordinly add a new key value or update the key value pair.

**Complexity Analysis**:
- **Algorithm**: Loop over the records and add each phone number to the dictionary. Add new key value or update already existing key. Laer loop over the key to find max time value.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the array.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the array size.


## Task3
**Description**: This is a 2 part problem. Part A is to identify the different area codes called by bangalore land lines (area code 080) and print then in order. Part B is it identify what percentage of calls are made from bangalore land line to other banglaoe landlines compared to total calls from bangalore landline.

**Approach**: Part A :Identify the call is from bangalore land line i.e. areacode (080). get the destination phone area code; if the next phone number starts with ( then check when it closes and capture the inbetween digits, else it is cell phone and capture first 4 digits. Add these to a set and then sort and print it.
Part B: check if the phone number starts with bangalore area code i.e. areacode (080). If yes add the total call by 1, check if the destination area code is bangalore then adde the bangalore calls by 1. Use these to calculate percent and show.


**Complexity Analysis**:
- **Algorithm**: Loop over the records and add each phone number to the set. 
- **Big O Notation**: $O(n + k log k)$ where n is the number of call records and k is the number of unique codes.
- **Justification**: We use sort, so the Big O is n log n.

## Task4
**Description**: Identify telemarketers by reviewing number that never receive a call or send/receive a text message.

**Approach**: Add phone numbers to a set. Discard the following numbers:
    Those number that received a call
    Those numbers that send or received a text
print the number in sorted order


**Complexity Analysis**:
- **Algorithm**: Loop over the records and add each phone number to the set. Then go over the set and discard the numbers and texts
- **Big O Notation**: $O(n + m+  k log )$ where n is the number of call records, m is the number of text records and k is the number of possible telemarketers.
- **Justification**: We use sort, so the Big O is n log n.


