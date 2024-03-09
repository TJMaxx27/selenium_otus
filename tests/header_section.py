from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderSection:
    def __init__(self, browser):
        self.browser = browser

    def click_my_account(self):
        my_account = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="My Account"]'))
        )
        my_account.click()

    def is_register_displayed(self):
        register = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Register"]'))
        )
        return register

    def is_login_displayed(self):
        login = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Login"]'))
        )
        return login

    def change_currency(self, currency_name):
        currency_dropdown = self.browser.find_element(
            By.XPATH, "//nav/div/div[1]/ul/li[1]/form/div/a/span"
        )
        currency_dropdown.click()

        currency_option = self.browser.find_element(
            By.XPATH, f'//a[@href="{currency_name}"]'
        )
        currency_option.click()

    def is_currency_changed(self, expected_currency):
        actual_currency = self.browser.find_element(
            By.XPATH, "//nav/div/div[1]/ul/li[1]/form/div/a/span"
        ).text
        return actual_currency == expected_currency
