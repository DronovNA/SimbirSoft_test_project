import csv

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_login_button = (
            By.XPATH,
            "//button[contains(text(),'Customer Login')]",
        )
        self.username_input = (By.ID, "userSelect")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def click_customer_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.customer_login_button)
        ).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

class BankOperations:
    def __init__(self, driver):
        self.driver = driver

    def deposit(self, amount):
        deposit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='deposit()']"))
        )
        deposit_button.click()
        deposit_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='amount']")
            )
        )
        deposit_input.clear()
        deposit_input.send_keys(amount)
        deposit_submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and text()='Deposit']")
            )
        )
        deposit_submit.click()

    def withdrawal(self, amount):
        withdrawal_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='withdrawl()']"))
        )
        withdrawal_button.click()

        withdrawal_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//label[text()='Amount to be Withdrawn :']/following-sibling::input[@placeholder='amount']",
                )
            )
        )
        withdrawal_input.clear()
        withdrawal_input.send_keys(amount)

        withdrawal_submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and text()='Withdraw']")
            )
        )
        withdrawal_submit.click()


    """
    Принято во внимание, что использование длинного CSS-селектора здесь не является предпочтительным подходом,
    так как он может быть хрупким и перестать работать при изменении структуры страницы.
    
    Однако, в данном случае других уникальных идентификаторов для элемента не было найдено.
    Рекомендуется искать более устойчивые способы идентификации элементов.
    """
    def check_balance(self, expected_balance):
        balance_element = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)",
        )
        current_balance = balance_element.text
        assert current_balance == str(
            expected_balance
        ), f"Текущий баланс ({current_balance}) не равен ожидаемому ({expected_balance})"

    def test_check_transactions_and_export_to_csv(self):
        transaction_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='transactions()']"))
        )
        transaction_button.click()

        transaction_elements = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[contains(@id, 'anchor')]"))
        )

        transactions_data = [
            ["Дата-времяТранзакции", "Сумма", "ТипТранзакции"]
        ]

        for transaction_element in transaction_elements:
            transaction_info = transaction_element.text
            transactions_data.append([transaction_info])

        with open('transactions.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(transactions_data)

        allure.attach.file('transactions.csv', name='Transaction Data CSV', attachment_type=allure.attachment_type.CSV)

        allure.attach("Транзакции успешно проверены", name="Проверка транзакций",
                      attachment_type=allure.attachment_type.TEXT)


