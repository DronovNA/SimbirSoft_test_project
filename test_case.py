import allure

from page_objects import BankOperations
from utils import FibonacciCalculator


@allure.story("Loggin Harry")
def test_login(logged_in_driver):
    pass

@allure.story("Bank Operations")
def test_bank_operations(logged_in_driver):
    bank_operations = BankOperations(logged_in_driver)

    fibonacci_number = FibonacciCalculator.calculate()
    bank_operations.deposit(fibonacci_number)

    withdrawal_amount = fibonacci_number
    bank_operations.withdrawal(withdrawal_amount)

    expected_balance = fibonacci_number - withdrawal_amount
    bank_operations.check_balance(expected_balance)

    bank_operations.test_check_transactions_and_export_to_csv()

