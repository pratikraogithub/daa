def is_safe(board, row, col, n):
    # Check if there is a Queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        # All Queens are placed successfully
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place Queen in this position
            board[row][col] = 1

            # Recur to place Queens in the next rows
            if solve_n_queens_util(board, row + 1, n):
                return True

            # If placing Queen in the current position doesn't lead to a solution, backtrack
            board[row][col] = 0
    
    return False

def solve_n_queens(n):
    # Initialize the board with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place the first Queen in the first row (row = 0)
    board[0][0] = 1

    # Call the recursive utility function to solve the remaining Queens
    if not solve_n_queens_util(board, 1, n):
        print(f"No solution exists for {n}-Queens.")
        return None

    return board

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

if __name__ == "__main__":
    n = int(input("Enter the value of n for n-Queens: "))
    
    if n < 1:
        print("Please enter a valid value for n.")
    else:
        final_board = solve_n_queens(n)
        if final_board:
            print(f"\nSolution for {n}-Queens:")
            print_board(final_board)
