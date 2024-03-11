from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from header_section import HeaderSection
import random


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.header = HeaderSection(browser)

    def load(self):
        self.browser.get("http://192.168.1.6:8081/")

    def is_logo_displayed(self):
        return self._is_element_displayed(
            By.CSS_SELECTOR,
            'img[src="http://192.168.1.6:8081/image/catalog/opencart-logo.png"]',
        )

    def is_search_field_displayed(self):
        return self._is_element_displayed(By.ID, "search")

    def is_cart_displayed(self):
        return self._is_element_displayed(By.ID, "header-cart")

    def is_carousel_displayed(self):
        return self._is_element_displayed(By.ID, "carousel-banner-0")

    def is_macbook_image_displayed(self):
        return self._is_element_displayed(
            By.CSS_SELECTOR,
            'img[src="http://192.168.1.6:8081/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg"]',
        )

    def is_iphone_image_displayed(self):
        return self._is_element_displayed(
            By.CSS_SELECTOR,
            'img[src="http://192.168.1.6:8081/image/cache/catalog/demo/banners/iPhone6-1140x380.jpg"]',
        )

    def is_logout_displayed(self):
        return self._is_element_displayed(
            By.XPATH,
            'a.list-group-item[href^="http://192.168.1.6:8081/en-gb?route=account/logout"]',
        )

    def add_random_product_to_cart(self):
        xpath_list = [
            '//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div/button[1]',
            '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]',
        ]

        random_xpath = random.choice(xpath_list)

        add_to_cart_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, random_xpath))
        )

        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", add_to_cart_button
        )

        while True:
            try:
                add_to_cart_button.click()
                break
            except ElementClickInterceptedException:
                add_to_cart_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, random_xpath))
                )

    def is_product_added_to_cart(self):
        return WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#header-cart .dropdown-toggle"), "1 item(s)"
            )
        )

    def get_product_prices(self):
        return [
            price.text
            for price in self.browser.find_elements(By.CSS_SELECTOR, ".price-new")
        ]

    def _is_element_displayed(self, by, value):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False
