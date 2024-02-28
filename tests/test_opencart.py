from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import is_element_displayed
from config import ADMIN_PASSWORD, ADMIN_USERNAME
import time
import random


def test_home_page(browser):
    # Переход на главную страницу
    browser.get("http://192.168.1.6:8081/")
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    # Проверка наличия логотипа
    assert is_element_displayed(
        browser,
        By.CSS_SELECTOR,
        'img[src="http://192.168.1.6:8081/image/catalog/opencart-logo.png"]',
    ), "Логотип не отображается"

    # Проверка наличия поля поиска
    assert is_element_displayed(browser, By.ID, "search"), "Поле поиска не отображается"

    # Проверка наличия корзины
    assert is_element_displayed(
        browser, By.ID, "header-cart"
    ), "Корзина не отображается"

    # Проверка карусели
    assert is_element_displayed(
        browser, By.ID, "carousel-banner-0"
    ), "Карусель не отображается"

    # Проверка фото в карусели
    assert is_element_displayed(
        browser,
        By.CSS_SELECTOR,
        'img[src="http://192.168.1.6:8081/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg"]',
    ), "Фото MacBook не отображается"

    assert is_element_displayed(
        browser,
        By.CSS_SELECTOR,
        'img[src="http://192.168.1.6:8081/image/cache/catalog/demo/banners/iPhone6-1140x380.jpg"]',
    ), "Фото iPhone не отображается"

    # Проверка выпадающего списка "My Account"
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//span[text()="My Account"]'))
    ).click()
    assert is_element_displayed(
        browser, By.XPATH, '//a[text()="Register"]'
    ), "Регистрация в списке отсутствует"
    assert is_element_displayed(
        browser, By.XPATH, '//a[text()="Login"]'
    ), "Авторизация в списке отсутствует"


def test_catalog_laptop_notebooks(browser):
    browser.get("http://192.168.1.6:8081/")
    wait = WebDriverWait(browser, 1, poll_frequency=1)

    # Проверка перехода с главной страницы
    laptops_and_notebooks = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(), 'Laptops & Notebooks')]")
        )
    )
    laptops_and_notebooks.click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(), 'Show All Laptops & Notebooks')]")
        )
    ).click()

    # Проверка открытия каталога Laptops & Notebooks
    assert is_element_displayed(
        browser, By.XPATH, '//h2[text()="Laptops & Notebooks"]'
    ), "Laptops & Notebooks не отображается"

    # Проверка отображения списка продуктов
    assert is_element_displayed(browser, By.ID, "product-list")

    # Проверка отображения фото товаров в списке продуктов
    products = browser.find_elements(By.CSS_SELECTOR, "#product-list .product-thumb")
    for product in products:
        image = product.find_element(By.CSS_SELECTOR, 'img[src$=".jpg"]')
        assert image.is_displayed(), "Фото товара не отображается"

    # Проверка нажатие на кнопку "List" и отображения товара списком
    wait.until(EC.visibility_of_element_located((By.ID, "button-list"))).click()
    element = wait.until(EC.visibility_of_element_located((By.ID, "product-list")))
    assert element.get_attribute("class") == "row row-cols-1 product-list"


def test_product_info_hp_lp3065(browser):
    browser.get("http://192.168.1.6:8081/en-gb/catalog/laptop-notebook")
    wait = WebDriverWait(browser, 1, poll_frequency=1)

    # Проверка открытия карточки товара
    card_hp_lp3065 = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(), 'HP LP3065')]")
        )
    )
    card_hp_lp3065.click()
    assert (
        browser.current_url
        == "http://192.168.1.6:8081/en-gb/product/laptop-notebook/hp-lp3065"
    ), f"URL не соответствует ожидаемому"

    # Проверка фото товара
    assert is_element_displayed(
        browser,
        By.CSS_SELECTOR,
        'img[src="http://192.168.1.6:8081/image/cache/catalog/demo/hp_1-500x500.jpg"]',
    ), "Фото не отображается"
    # Проверка отображения цены
    assert is_element_displayed(
        browser, By.CSS_SELECTOR, "span.price-new"
    ), "Цена не отображается"

    # Проверка отображения календаря
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.form-control.date"))
    ).click()
    assert is_element_displayed(
        browser,
        By.CSS_SELECTOR,
        ".daterangepicker.ltr.auto-apply.single.opensright.show-calendar",
    ), "Календарь не отображается"

    # Проверка отображения кнопки
    assert is_element_displayed(
        browser, By.XPATH, '//*[@id="button-cart"]'
    ), "Кнопка не отображается"


def test_administration_login(browser):
    browser.get("http://192.168.1.6:8081/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)
    # Отображение лого
    assert is_element_displayed(
        browser, By.CSS_SELECTOR, 'img[src="view/image/logo.png"]'
    )

    # Отображение заголовка
    assert is_element_displayed(browser, By.CSS_SELECTOR, ".card-header")

    # Проверка поля ввода логина
    assert is_element_displayed(browser, By.ID, "input-username")

    # Проверка поля ввода пароля
    assert is_element_displayed(browser, By.ID, "input-password")

    # Проверка кнопки Login
    assert is_element_displayed(browser, By.CLASS_NAME, "btn-primary")

    # Авторизация администратора
    browser.find_element(By.ID, "input-username").send_keys(ADMIN_USERNAME)
    browser.find_element(By.ID, "input-password").send_keys(ADMIN_PASSWORD)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Dashboard']"))
    ), "Авторизация не удалась"

    # Разлогирование
    browser.find_element(By.LINK_TEXT, "Logout").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-header")))


def test_register_account(browser):
    browser.get("http://192.168.1.6:8081/index.php?route=account/register")
    # Проверка поля Name
    assert is_element_displayed(browser, By.ID, "input-firstname")
    # Проверка поля Last Name
    assert is_element_displayed(browser, By.ID, "input-lastname")
    # Проверка поля E-mail
    assert is_element_displayed(browser, By.ID, "input-email")
    # Проверка поля Password
    assert is_element_displayed(browser, By.ID, "input-password")
    # Проверка кнопки "Continue"
    assert is_element_displayed(browser, By.CLASS_NAME, "btn-primary")


def test_add_random_product_to_cart(browser):
    browser.get("http://192.168.1.6:8081/")
    wait = WebDriverWait(browser, 5, poll_frequency=1)

    # Список с XPath кнопок "Add to Cart"
    xpath_list = [
        '//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div/button[1]',
        '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]',
    ]

    random_xpath = random.choice(xpath_list)

    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, random_xpath))
    )

    browser.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(0.5)

    add_to_cart_button.click()
    time.sleep(0.5)

    shopping_cart_item = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
        )
    )
    shopping_cart_item_text = shopping_cart_item.text
    expected_item = "1 item(s)"
    assert expected_item in shopping_cart_item_text, f"Товар не найден в корзине"


def test_currency_change_main_page(browser):
    browser.get("http://192.168.1.6:8081/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    product_price_before = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
    )
    price_before_change = [price.text for price in product_price_before]

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//nav/div/div[1]/ul/li[1]/form/div/a/span")
        )
    ).click()
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".dropdown-menu.show li:nth-child(1) a.dropdown-item")
        )
    ).click()

    product_price_after = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
    )
    price_after_change = [price.text for price in product_price_after]

    assert price_after_change != price_before_change, "Цена не изменилась"


def test_currency_change_catalog_desktops_page(browser):
    browser.get("http://192.168.1.6:8081/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 10, poll_frequency=1)

    wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                '#input-limit option[value="http://192.168.1.6:8081/en-gb/catalog/desktops?limit=25"]',
            )
        )
    ).click()

    product_price_before = wait.until(
        EC.presence_of_all_elements_located((By.ID, "product-list"))
    )
    price_before_change = [price.text for price in product_price_before]

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//nav/div/div[1]/ul/li[1]/form/div/a/span")
        )
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".dropdown-menu.show li:nth-child(2) a.dropdown-item")
        )
    ).click()

    product_price_after = wait.until(
        EC.presence_of_all_elements_located((By.ID, "product-list"))
    )
    price_after_change = [price.text for price in product_price_after]

    assert price_after_change != price_before_change, "Цена не изменилась"
