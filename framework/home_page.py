from .page import Page
from selenium.webdriver.common.by import By


class HomePage(Page):
    LOGIN_BUTTON = (By.ID, 'authHelloLogin')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_button_login(self):
        self.click_element(HomePage.LOGIN_BUTTON)
