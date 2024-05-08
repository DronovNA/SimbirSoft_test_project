import pytest
from selenium import webdriver

from page_objects import LoginPage


@pytest.fixture(scope="module")
def driver():
    remote_url = "http://192.168.1.64:4444/wd/hub"
    capabilities = {
        "browserName": "chrome",
        "platform": "ANY"
    }
    driver = webdriver.Remote(command_executor=remote_url, options=capabilities)
    yield driver
    driver.quit()



@pytest.fixture(scope="class")
def logged_in_driver(driver):
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    login_page = LoginPage(driver)
    login_page.click_customer_login_button()
    login_page.enter_username('HarryPotter')
    login_page.click_login_button()
    yield driver
