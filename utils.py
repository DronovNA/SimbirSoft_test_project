import datetime


class FibonacciCalculator:
    @staticmethod
    def calculate():
        current_day = datetime.datetime.now().day
        if current_day < 1:
            return 0
        elif current_day == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, current_day + 2):
                a, b = b, a + b
            return b
