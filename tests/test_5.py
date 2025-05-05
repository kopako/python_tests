import unittest

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('driver')
class IframeTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.driver.implicitly_wait(3)

    def test_iframe_text(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
        iframe = self.driver.find_element(By.ID, "my-iframe")
        self.driver.switch_to.frame(iframe)
        paragraphs = self.driver.find_elements(By.TAG_NAME, "p")
        expected_text = "semper posuere integer et senectus justo curabitur."
        found = any(expected_text in p.text for p in paragraphs)
        assert found

    def test_drag_drop(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Consent']").click()
        iframe = self.driver.find_element(By.CLASS_NAME, "demo-frame")
        self.driver.switch_to.frame(iframe)
        photo = self.driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]")
        trash = self.driver.find_element(By.ID, "trash")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(photo, trash).perform()
        # time.sleep(2)
        photos_in_trash = len(self.driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li"))
        photos_in_gallery = len(self.driver.find_elements(By.XPATH, "//ul[@id='gallery']/li"))
        assert photos_in_trash == 1
        assert photos_in_gallery == 3