# Program to calculate Fibonacci numbers using both recursive and non-recursive (iterative) approaches
# and analyze their time and space complexity.

# Recursive function to calculate Fibonacci numbers
def recur(n):
    if n <= 1:
        return n
    else:
        return recur(n-1) + recur(n-2)

# Iterative function to calculate Fibonacci numbers
def iterative(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(2, n):
        print(a + b)
        a, b = b, a + b

if __name__ == "__main__":
    # User input for the nth number in the Fibonacci series
    num = int(input("Enter the nth number for the series: "))

    # Check if the input is a positive integer
    if num <= 0:
        print("Please enter a positive integer")
    else:
        # Fibonacci sequence with recursion
        print("Fibonacci sequence with recursion:")
        for i in range(num):
            print(recur(i))

        # Fibonacci series with iteration
        print("Fibonacci series with iteration:")
        iterative(num)
