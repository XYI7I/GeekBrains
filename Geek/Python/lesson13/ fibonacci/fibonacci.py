"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""

import logging
import sys

logging.basicConfig(filename='fibonacci.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
        self.message = f"Invalid input: {input_value}"
        super().__init__(self.message)


class FibonacciCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate(n):
        if n <= 0:
            raise InvalidInputError(n)

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
        calculator = FibonacciCalculator()
        result = calculator.calculate(n)
        logging.info(f"Fibonacci({n}) = {result}")
        print(f"Fibonacci({n}) = {result}")
    except ValueError:
        input_value = sys.argv[1]
        logging.error(f"Invalid input: n should be an integer, received {input_value}")
        print("Error: Invalid input. n should be an integer.")
    except InvalidInputError as e:
        input_value = e.input_value
        logging.error(e.message)
        print(f"Error: {e.message}")
