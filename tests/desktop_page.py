from selenium.webdriver.common.by import By
from header_section import HeaderSection


class DesktopsPage:
    def __init__(self, browser):
        self.browser = browser
        self.header = HeaderSection(browser)

    def load(self):
        self.browser.get("http://192.168.1.6:8081/en-gb/catalog/desktops")

    def change_currency_to_poland_sterling(self):
        currency_dropdown = self.browser.find_element(
            By.XPATH, "//nav/div/div[1]/ul/li[1]/form/div/a/span"
        )
        currency_dropdown.click()
        eur_option = self.browser.find_element(
            By.CSS_SELECTOR, ".dropdown-menu.show li:nth-child(2) a.dropdown-item"
        )
        eur_option.click()

    def get_product_prices(self):
        return [
            price.text for price in self.browser.find_elements(By.ID, "product-list")
        ]
