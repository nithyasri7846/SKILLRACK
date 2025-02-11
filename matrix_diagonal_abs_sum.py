'''Absolute difference of the sum across the diagonals 
You are given a square matrix of size N×N. Calculate the absolute difference of the sums across the two main diagonals. Boundary Condition(s): 2 <= N <= 20 Input Format: The first line will contain the value of N. The next N lines will contain the N values separated by one or more spaces. Output Format: The absolute difference of the sums across the two main diagonals. Example Input/Output 1: Input: 2 10 9 4 22 Output: 19 Explanation: The sum along the first main diagonal is 10+22 = 32. The sum along the second main diagonal is 4+9=13. The absolute difference is 32-13= 19. Example Input/Output 2: Input: 2 -10 6 4 -22 Output: 22'''
n = int(input().strip())
matrix = [list(map(int, input().split())) for i in range(n)]

# Sum the diagonal elements normally (without taking the absolute value first)
sum_diag1 = sum(matrix[i][i] for i in range(n))
sum_diag2 = sum(matrix[i][n-1-i] for i in range(n))

# Now take the absolute value of the sums and calculate their difference
result = abs(abs(sum_diag1) - abs(sum_diag2))
print(result)

