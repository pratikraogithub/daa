"""
Fractional Knapsack Problem

You are given weights and values of 'n' items, and a knapsack with a maximum capacity 'M'.
Implement a program to solve the fractional knapsack problem using a greedy approach.

- Each item is represented by its weight and value.
- The goal is to maximize the total value of items in the knapsack without exceeding its capacity.
- You can take fractions of items to maximize the total value.

The program takes user input for the number of items, their weights, values, and the capacity of the knapsack.
It then applies the fractional knapsack algorithm and prints the selected items along with the maximum total value.

Author: Your Name
"""

class KnapsackPackage(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight
    
    def __lt__(self, other):
        # Custom comparison method to sort packages by cost in descending order
        return self.cost < other.cost

class FractionalKnapsack(object):
    def knapsackGreProc(self, W, V, M, n):
        # Create KnapsackPackage objects for each item
        packs = [KnapsackPackage(W[i], V[i]) for i in range(n)]
        
        # Sort packages by cost in descending order
        packs.sort(reverse=True)
        
        remain = M
        result = 0
        i = 0
        stopProc = False
        
        while not stopProc:
            if packs[i].weight <= remain:
                # Take the whole package if it fits into the knapsack
                remain -= packs[i].weight
                result += packs[i].value
                print(f"Pack {i} - Weight {packs[i].weight} - Value {packs[i].value}")
            
            if packs[i].weight > remain:
                # Move to the next package if the current one doesn't fit entirely
                i += 1
            
            if i == n:
                # Stop if all packages are considered
                stopProc = True
        
        print("Max Value:\t", result)

if __name__ == "__main__":
    # User input for the number of items, weights, values, and knapsack capacity
    W = []
    V = []
    num = int(input("Enter the number of weights or values required:\n"))
    
    for i in range(num):
        w = int(input(f"Enter weight {i + 1}: "))
        v = int(input(f"Enter value {i + 1}: "))
        W.append(w)
        V.append(v)
    
    M = int(input("Enter the capacity of the knapsack: "))
    
    # Solve the fractional knapsack problem
    proc = FractionalKnapsack()
    proc.knapsackGreProc(W, V, M, num)
