'''You are given a square matrix of size N×N. Calculate the sum of the integers present in the two main diagonals. Input Format: The first line will contain the value of N. The next N lines will contain the N values separated by one or more spaces. Output Format: The sum of the integers present in the two main diagonals. Boundary Conditions: 2 <= N <= 20 Example Input/Output 1: Input: 2 10 9 4 22 Output: 45 Explanation: The sum is = 10+22+9+4 = 45 Example Input/Output 2: Input: 3 5 10 11 79 6 12 9 21 45 Output: 76 Explanation: The sum is = 5+6+45+11+9 = 76. As 6 is common for both the diagonals it must be counted only once when finding the sum.'''

# Step 1: Read the size of the square matrix.
n = int(input().strip())

# Step 2: Read the matrix.
# For each of the n rows, split the input line into integers and store it as a list.
matrix = [list(map(int, input().split())) for _ in range(n)]

# Step 3: Initialize the total sum to 0.
total = 0

# Step 4: Iterate over each row to add the elements of both diagonals.
for i in range(n):
    # matrix[i][i] is the element on the main (primary) diagonal.
    # matrix[i][n-1-i] is the element on the secondary diagonal.
    # If the current element is the common element (which happens when i == n-1-i, i.e., at the center of an odd-sized matrix),
    # add it only once.
    if i == n - 1 - i:
        total += matrix[i][i]
    else:
        total += matrix[i][i] + matrix[i][n - 1 - i]

# Step 5: Print the final sum of the diagonal elements.
print(total)


