import multiprocessing
import time

def square_number(number):
    return number ** 2

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(square_number, numbers)  # Perform the task in parallel
    print(results)  # Output: [1, 4, 9, 16, 25]