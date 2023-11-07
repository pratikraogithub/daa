"""
0-1 Knapsack Problem using Dynamic Programming

You are given a set of items, each with a weight (wt) and a value (val).
The goal is to maximize the total value that can be included in the knapsack
while keeping the total weight within a given limit (W).

Implement a program to solve the 0-1 Knapsack problem using dynamic programming.

Author: Your Name
"""

def knapSack(W, wt, val, n):
    # Create a 1D list to store the maximum value achievable for each weight
    dp = [0 for i in range(W + 1)]

    # Build the dp list using bottom-up dynamic programming
    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]

if __name__ == "__main__":
    # User input for the number of items, weights, and values
    W = []
    V = []
    num = int(input("Enter the number of weights or values required:\n"))

    # Input weights
    for i in range(num):
        n = int(input(f"Enter weight {i + 1}: "))
        W.append(n)

    print("\n")

    # Input values
    for i in range(num):
        n = int(input(f"Enter value {i + 1}: "))
        V.append(n)

    print("\n")

    # Input knapsack capacity
    knapsack_capacity = int(input("Enter the capacity of the knapsack: "))

    # Solve the 0-1 Knapsack problem
    max_value = knapSack(knapsack_capacity, W, V, num)

    print("Maximum value in Knapsack =", max_value)
 