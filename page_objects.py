import allure

from page_locators import LoginPageLocators, BankOperationsPageLocators
from utils import write_transactions_to_csv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverWaitHelper:
    def __init__(self, driver):
        self.driver = driver
        self.default_wait_time = 10

    def wait_for_element_clickable(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_wait_time
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visible(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_wait_time
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_all_elements_visible(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_wait_time
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_login_button = LoginPageLocators.CUSTOMER_LOGIN_BUTTON
        self.username_input = LoginPageLocators.USERNAME_INPUT
        self.login_button = LoginPageLocators.LOGIN_BUTTON
        self.wait_helper = WebDriverWaitHelper(self.driver)

    @allure.step("Click Customer Login Button")
    def click_customer_login_button(self):
        self.wait_helper.wait_for_element_clickable(self.customer_login_button).click()

    @allure.step("Enter Username: {username}")
    def enter_username(self, username):
        self.wait_helper.wait_for_element_visible(self.username_input).send_keys(
            username
        )

    @allure.step("Click Login Button")
    def click_login_button(self):
        self.wait_helper.wait_for_element_clickable(self.login_button).click()


class BankOperations:
    def __init__(self, driver):
        self.driver = driver
        self.wait_helper = WebDriverWaitHelper(self.driver)

    @allure.step("Click Deposit Button")
    def click_deposit_button(self):
        self.wait_helper.wait_for_element_clickable(
            BankOperationsPageLocators.DEPOSIT_BUTTON
        ).click()

    @allure.step("Enter Deposit Amount: {amount}")
    def enter_deposit_amount(self, amount):
        deposit_input = self.wait_helper.wait_for_element_clickable(
            BankOperationsPageLocators.AMOUNT_INPUT
        )
        deposit_input.clear()
        deposit_input.send_keys(amount)

    @allure.step("Confirm Deposit")
    def confirm_deposit(self):
        self.wait_helper.wait_for_element_clickable(
            BankOperationsPageLocators.DEPOSIT_SUBMIT_BUTTON
        ).click()

    @allure.step("Click Withdrawal Button")
    def click_withdrawal_button(self):
        self.wait_helper.wait_for_element_clickable(
            BankOperationsPageLocators.WITHDRAWAL_BUTTON
        ).click()

    @allure.step("Enter Withdrawal Amount: {amount}")
    def enter_withdrawal_amount(self, amount):
        withdrawal_input = self.wait_helper.wait_for_element_visible(
            BankOperationsPageLocators.AMOUNT_INPUT
        )
        withdrawal_input.clear()
        withdrawal_input.send_keys(amount)

    @allure.step("Confirm Withdrawal")
    def confirm_withdrawal(self):
        self.wait_helper.wait_for_element_clickable(
            BankOperationsPageLocators.WITHDRAWAL_SUBMIT_BUTTON
        ).click()

    # @allure.step("Make a Withdrawal of {amount}")
    # def withdrawal(self, amount):
    #     self.click_withdrawal_button()
    #     self.enter_withdrawal_amount(amount)
    #     self.confirm_withdrawal()

    @allure.step("Check Balance: {expected_balance}")
    def check_balance(self, expected_balance):
        balance_element = self.driver.find_element(
            *BankOperationsPageLocators.BALANCE_ELEMENT
        )
        current_balance = balance_element.text
        assert current_balance == str(
            expected_balance
        ), f"Текущий баланс ({current_balance}) не равен ожидаемому ({expected_balance})"

    @allure.step("Test Check Transactions and Export to CSV")
    def test_check_transactions_and_export_to_csv(self):
        transaction_button = self.wait_helper.wait_for_element_clickable(
            BankOperationsPageLocators.TRANSACTION_BUTTON
        )
        transaction_button.click()
        transaction_elements = self.wait_helper.wait_for_all_elements_visible(
            BankOperationsPageLocators.TRANSACTION_ELEMENTS
        )

        transactions_data = [["Дата-времяТранзакции", "Сумма", "ТипТранзакции"]]

        for transaction_element in transaction_elements:
            transaction_info = transaction_element.text
            transactions_data.append([transaction_info])

        write_transactions_to_csv(transactions_data)

        allure.attach.file(
            "transactions.csv",
            name="Transaction Data CSV",
            attachment_type=allure.attachment_type.CSV,
        )

        allure.attach(
            "Транзакции успешно проверены",
            name="Проверка транзакций",
            attachment_type=allure.attachment_type.TEXT,
        )
