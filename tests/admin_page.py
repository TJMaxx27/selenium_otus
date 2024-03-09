from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("http://192.168.1.6:8081/administration/")

    def is_logo_displayed(self):
        return self._is_element_displayed(
            By.CSS_SELECTOR, 'img[src="view/image/logo.png"]'
        )

    def is_header_displayed(self):
        return self._is_element_displayed(By.CSS_SELECTOR, ".card-header")

    def is_username_field_displayed(self):
        return self._is_element_displayed(By.ID, "input-username")

    def is_password_field_displayed(self):
        return self._is_element_displayed(By.ID, "input-password")

    def is_login_button_displayed(self):
        return self._is_element_displayed(By.CLASS_NAME, "btn-primary")

    def login(self, username, password):
        self.browser.find_element(By.ID, "input-username").send_keys(username)
        self.browser.find_element(By.ID, "input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
        )

    def is_dashboard_displayed(self):
        return self._is_element_displayed(By.XPATH, "//h1[text()='Dashboard']")

    def go_to_catalog_and_products(self):
        catalog_menu = self.browser.find_element(
            By.CSS_SELECTOR, 'a.parent[href="#collapse-1"][data-bs-toggle="collapse"]'
        )
        catalog_menu.click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//a[contains(@href, "catalog/product")]')
            )
        )

        products_menu = self.browser.find_element(
            By.XPATH, '//a[contains(@href, "catalog/product")]'
        )
        return products_menu

    def add_new_product_button(self):
        add_new_product_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-solid.fa-plus"))
        )
        return add_new_product_button

    def add_product(self):
        self.browser.find_element(By.ID, "input-name-1").send_keys("iPhoneXs_test")
        self.browser.find_element(By.ID, "input-meta-title-1").send_keys(
            "iPhoneXs_test"
        )
        self.browser.find_element(
            By.CSS_SELECTOR, 'a.nav-link[href="#tab-data"]'
        ).click()
        self.browser.find_element(By.ID, "input-model").send_keys("iPhoneXs_test")
        self.browser.find_element(
            By.CSS_SELECTOR, 'a.nav-link[aria-selected="false"][href="#tab-seo"]'
        ).click()
        self.browser.find_element(By.ID, "input-keyword-0-1").send_keys("iPhoneXS")

    def save_button(self):
        return self.browser.find_element(
            By.XPATH,
            "//button[@type='submit' and @form='form-product' and contains(@title, 'Save')]",
        )

    def find_test_product_in_products(self):
        return self.browser.find_element(
            By.XPATH, f"//td[contains(text(), 'iPhoneXs_test')]/.."
        )

    def find_checkbox_test_product(self):
        test_product_row = self.find_test_product_in_products()
        return test_product_row.find_element(
            By.CSS_SELECTOR, 'input[type="checkbox"][name="selected[]"]'
        )

    def delete_button(self):
        return self.browser.find_element(By.XPATH, "//button[@title='Delete']")

    def alert_window_success(self):
        alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert.accept()
        return alert

    def modified_popup(self):
        modified_popup = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
            )
        )
        return modified_popup

    def logout(self):
        self.browser.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".card-header"))
        )

    def _is_element_displayed(self, by, value):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False
