from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Customer Login')]")
    USERNAME_INPUT = (By.ID, "userSelect")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")


class BankOperationsPageLocators:
    DEPOSIT_BUTTON = (By.XPATH, "//button[@ng-click='deposit()']")
    WITHDRAWAL_BUTTON = (By.XPATH, "//button[@ng-click='withdrawl()']")
    BALANCE_ELEMENT = (
        By.CSS_SELECTOR,
        "body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)",
    )
    TRANSACTION_BUTTON = (By.XPATH, "//button[@ng-click='transactions()']")
    TRANSACTION_ELEMENTS = (By.XPATH, "//*[contains(@id, 'anchor')]")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='amount']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    DEPOSIT_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Deposit']")
    WITHDRAWAL_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and text()='Withdraw']",
    )
