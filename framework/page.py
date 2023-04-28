from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_data(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
