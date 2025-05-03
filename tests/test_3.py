import unittest

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('driver')
class WebPageTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.driver.implicitly_wait(3)
        self.driver.get("https://itcareerhub.de/ru")


    def test_logo(self):
        element = self.driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310155")
        assert element, "logo is not found"

    def test_programs(self):
        element = self.driver.find_element(By.LINK_TEXT, 'Программы')
        assert element, "Programs link not found"

    def test_payment(self):
        element = self.driver.find_element(By.LINK_TEXT, 'Способы оплаты')
        assert element, "Payment link not found"

    def test_news(self):
        element = self.driver.find_element(By.LINK_TEXT, 'Новости')
        assert element, "News link not found"

    def test_about_us(self):
        element = self.driver.find_element(By.LINK_TEXT, 'О нас')
        assert element, "About us link not found"

    def test_reviews(self):
        element = self.driver.find_element(By.LINK_TEXT, 'Отзывы')
        assert element, "Reviews link not found"

    def test_ru(self):
        element = self.driver.find_element(By.LINK_TEXT, 'ru')
        assert element, "ru language link not found"

    def test_call(self):
        call_div_class = 'tn-elem__7178437221710153310161'
        call_element = self.driver.find_element(By.CLASS_NAME, call_div_class)
        call_element.click()
        popup_element = self.driver.find_element(By.XPATH, '//*[text()="Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"]')
        assert popup_element, "Popup element not found"

    def test_de(self):
        element = self.driver.find_element(By.LINK_TEXT, 'de')
        assert element, "de lang link not found"
