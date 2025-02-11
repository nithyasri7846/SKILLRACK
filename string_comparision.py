'''String - Letters comparison
Two string values S1 and S2 are passed as input. The program must check if both S1 and S2 contain the same unique set of letters and print YES or NO. Assume all the letters (alphabets) are in smaller case. Boundary Conditions: Length of S1 is from 2 to 100 Length of S2 is from 2 to 100 Input Format: First line will contain the string value of S1 Second line will contain the string value of S2 Output Format: YES or NO depending on if both S1 and S2 contain the same set of unique letters. IMPORTANT: Please note that the output is CASE SENSITIVE. Hence print YES or NO (instead of yes or no)
 Sample Input/Output: Example 1: Input: read dear Output: YES Explanation: Both S1 and S2 are formed using the letters - a d e r Example 2: Input: record decoder Output: YES Explanation: Both S1 and S2 are formed using the letters - c d e o r Example 3: Input: energy synergy Output: NO Explanation: S2 has additional letter - s in it.'''
PROGRAM:
# Read the two input strings
s1 = input().strip()
s2 = input().strip()

# Convert each string to a set of characters
set1 = set(s1)
set2 = set(s2)

# Check if both sets are equal and print the result
if set1 == set2:
    print("YES")
else:
    print("NO")
'''Explanation
Input Reading:
The program reads two strings using input().strip(), which removes any extra whitespace.

Unique Letters:
Each string is converted to a set using set(s1) and set(s2). This keeps only the unique characters.

Comparison:
The two sets are compared. If they are equal (i.e., both strings have the same unique letters), the program prints "YES". Otherwise, it prints "NO".

For example:

If s1 is "read" and s2 is "dear", both sets will be {'a', 'd', 'e', 'r'}, and the output will be YES.
If s1 is "energy" and s2 is "synergy", the sets will differ (the second contains an extra 's'), so the output will be NO.
This solution meets the problem requirements exactly.'''
