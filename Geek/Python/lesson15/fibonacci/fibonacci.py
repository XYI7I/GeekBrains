"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""

import logging
import sys

logging.basicConfig(filename='fibonacci.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fibonacci(n):
    if n <= 0:
        logging.error(f"Invalid input: n should be a positive integer, received {n}")
        return None

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        result = fibonacci(n)
        if result is not None:
            logging.info(f"Fibonacci({n}) = {result}")
            print(f"Fibonacci({n}) = {result}")
    except ValueError:
        logging.error(f"Invalid input: n should be an integer, received {sys.argv[1]}")
        print("Error: Invalid input. n should be an integer.")