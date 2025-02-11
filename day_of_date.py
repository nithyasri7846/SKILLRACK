# List mapping days to their indices
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# Read inputs
first_day = input().strip()  # e.g., "MON"
D = int(input().strip())     # e.g., 10

# Find the index corresponding to the first day of the month
start_index = days.index(first_day)

# Calculate the offset (number of days to move from the 1st to the D-th)
offset = D - 1

# Adjust offset by subtracting 7 repeatedly (simulate modulus)
while offset >= 7:
    offset -= 7

# Compute the new index for the D-th day
new_index = start_index + offset

# Adjust new_index similarly to wrap around if needed
while new_index >= 7:
    new_index -= 7

# Output the day corresponding to the D-th date
print(days[new_index])

#Output
'''Explanation with an Example
Example 1:

Input:
MON
10

Process:
start_index for "MON" is 0.
offset = 10 - 1 = 9.
Subtract 7 from 9: 9 - 7 = 2.
Add start_index and adjusted offset: 0 + 2 = 2.
The day at index 2 is "WED".

Output:
WED'''
