import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestPOM:

    @pytest.fixture(scope="class")
    def local_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--disable-gpu")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=options)
        LoginPage(driver).success_login()
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, local_driver):
        return InventoryPage(local_driver)

    @pytest.fixture(scope="class")
    def checkout_page(self, local_driver):
        return CheckoutPage(local_driver)

    @pytest.fixture(scope="class")
    def cart_page(self, local_driver):
        return CartPage(local_driver)

    def test_total_amount(self, inventory_page, checkout_page, cart_page):
        items = ['Sauce Labs Backpack',
                 'Sauce Labs Bolt T-Shirt',
                 'Sauce Labs Onesie']

        [inventory_page.add_item_to_cart(item) for item in items]
        inventory_page.go_to_cart()
        cart_page.proceed_to_checkout()
        checkout_page.fill_checkout_form()
        total = checkout_page.get_total_price()
        assert total == 58.29
