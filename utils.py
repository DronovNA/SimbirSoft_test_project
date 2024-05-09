import datetime
import csv


class FibonacciCalculator:
    @staticmethod
    def get_current_day_plus_one():
        return datetime.datetime.now().day + 1

    @staticmethod
    def calculate_fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b


def write_transactions_to_csv(transactions_data, filename="transactions.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(transactions_data)
