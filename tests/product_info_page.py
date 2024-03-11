from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductInfoPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("http://192.168.1.6:8081/en-gb/catalog/laptop-notebook")

    def click_hp_lp3065(self):
        card_hp_lp3065 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(), 'HP LP3065')]")
            )
        )
        card_hp_lp3065.click()

    def is_hp_lp3065_url(self):
        return (
            self.browser.current_url
            == "http://192.168.1.6:8081/en-gb/product/laptop-notebook/hp-lp3065"
        )

    def is_product_image_displayed(self):
        return self._is_element_displayed(
            By.CSS_SELECTOR,
            'img[src="http://192.168.1.6:8081/image/cache/catalog/demo/hp_1-500x500.jpg"]',
        )

    def is_price_displayed(self):
        return self._is_element_displayed(By.CSS_SELECTOR, "span.price-new")

    def is_calendar_displayed(self):
        return self._is_element_displayed(
            By.CSS_SELECTOR,
            ".daterangepicker.ltr.auto-apply.single.opensright.show-calendar",
        )

    def is_add_to_cart_displayed(self):
        return self._is_element_displayed(By.XPATH, '//*[@id="button-cart"]')

    def _is_element_displayed(self, by, value):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False
