import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def analyze_runtime(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr)
    end_time = time.time()
    runtime = end_time - start_time
    return sorted_arr, runtime

if __name__ == "__main__":
    # Generate a random list of numbers for testing
    input_array = [random.randint(0, 1000) for _ in range(1000)]

    # Analyze runtime for deterministic QuickSort
    sorted_arr_deterministic, runtime_deterministic = analyze_runtime(quicksort, input_array.copy())
    print(f"Deterministic QuickSort Runtime: {runtime_deterministic:.6f} seconds")

    # Analyze runtime for randomized QuickSort
    sorted_arr_randomized, runtime_randomized = analyze_runtime(randomized_quicksort, input_array.copy())
    print(f"Randomized QuickSort Runtime: {runtime_randomized:.6f} seconds")

    # Check if both versions produce the same result
    assert sorted_arr_deterministic == sorted_arr_randomized, "Sort results differ!"

    print("\nSorting Successful!")
