import unittest

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('driver')
class WebPageTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.driver.implicitly_wait(3)

    def test_button_new_name(self):
        self.driver.get("http://uitestingplayground.com/textinput")
        element_new_button_name = self.driver.find_element(By.ID, "newButtonName")
        element_new_button_name.send_keys("ITCH")
        element_button_set_name = self.driver.find_element(By.ID, "updatingButton")
        element_button_set_name.click()
        assert element_button_set_name.text == "ITCH", "Текст не изменился"

    def test_image_upload(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        wait = WebDriverWait(self.driver, 10)
        landscape = wait.until(EC.presence_of_element_located((By.ID, "landscape")))
        assert landscape
