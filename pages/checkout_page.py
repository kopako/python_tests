from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class CheckoutPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self):
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.clear()
        first_name_input.send_keys('name')
        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.clear()
        last_name_input.send_keys('surname')
        postal_code_input = self.driver.find_element(By.ID, 'postal-code')
        postal_code_input.clear()
        postal_code_input.send_keys('11111')
        self.driver.find_element(By.ID, 'continue').click()


    def get_total_price(self):
        total_amount_el = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label')))
        return float(total_amount_el.text.removeprefix('Total: $'))