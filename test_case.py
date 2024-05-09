import allure
from page_objects import BankOperations
from utils import FibonacciCalculator


@allure.story("Loggin Harry")
def test_login(logged_in_driver):
    pass


@allure.story("Bank Operations")
def test_bank_operations(logged_in_driver):
    bank_operations = BankOperations(logged_in_driver)

    current_day = FibonacciCalculator.get_current_day_plus_one()
    fibonacci_number = FibonacciCalculator.calculate_fibonacci(current_day)

    bank_operations.click_deposit_button()
    bank_operations.enter_deposit_amount(fibonacci_number)
    bank_operations.confirm_deposit()

    withdrawal_amount = fibonacci_number
    bank_operations.click_withdrawal_button()
    bank_operations.enter_withdrawal_amount(withdrawal_amount)
    bank_operations.confirm_withdrawal()

    expected_balance = fibonacci_number - withdrawal_amount
    bank_operations.check_balance(expected_balance)

    bank_operations.test_check_transactions_and_export_to_csv()
