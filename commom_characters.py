'''Two string values S1 and S2 are passed as input. The program must print the count of common characters in the strings S1 and S2. Input Format: First line will contain the value of string S1 Second line will contain the value of string S2 Output Format: First line will contain the count of common characters. Boundary Conditions: Length of S1 and S2 is from 3 to 100. Sample Input/Output: Example 1: Input: china india Output: 3 Explanation: The common characters are i,n,a Example 2: Input: energy every Output: 4 Explanation: The common characters are e,e,r,y'''

# Read the two input strings
s1 = input().strip()
s2 = input().strip()

# Initialize a counter for the common characters
common_count = 0

# For each unique character in s1,
# add the minimum number of occurrences in both strings.
for ch in set(s1):
    if ch in s2:
        common_count += min(s1.count(ch), s2.count(ch))

# Print the total count of common characters
print(common_count)

o/p:
'''Explanation
Counting Frequencies:
For each unique character in string a, we check if it appears in b. If it does, we add the minimum occurrence between a and b to common_count.

Example "delicacy" vs "celibacy":

'e' appears once in both strings → add 1
'l' appears once in both → add 1
'i' appears once in both → add 1
'c' appears twice in both → add 2
'a' appears once in both → add 1
'y' appears once in both → add 1
Total = 1 + 1 + 1 + 2 + 1 + 1 = 7
This way, the program correctly outputs 7 for your given input.'''
