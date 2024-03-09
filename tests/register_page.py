from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("http://192.168.1.6:8081/index.php?route=account/register")

    def is_name_field_displayed(self):
        return self._is_element_displayed(By.ID, "input-firstname")

    def enter_name(self, name):
        name_field = self.browser.find_element(By.ID, "input-firstname")
        name_field.clear()
        name_field.send_keys(name)

    def is_last_name_field_displayed(self):
        return self._is_element_displayed(By.ID, "input-lastname")

    def enter_last_name(self, last_name):
        last_name_field = self.browser.find_element(By.ID, "input-lastname")
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def is_email_field_displayed(self):
        return self._is_element_displayed(By.ID, "input-email")

    def enter_email(self, email):
        email_field = self.browser.find_element(By.ID, "input-email")
        email_field.clear()
        email_field.send_keys(email)

    def is_password_field_displayed(self):
        return self._is_element_displayed(By.ID, "input-password")

    def enter_password(self, password):
        password_field = self.browser.find_element(By.ID, "input-password")
        password_field.clear()
        password_field.send_keys(password)

    def privacy_policy_checkbox_agree(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, 'input[name="agree"][value="1"]'
        )

    def is_continue_button_displayed(self):
        return self._is_element_displayed(By.CLASS_NAME, "btn-primary")

    def continue_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

    def _is_element_displayed(self, by, value):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False
