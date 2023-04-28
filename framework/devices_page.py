from .page import Page
from selenium.webdriver.common.by import By


class DevicesPage(Page):
    ADD_HUB_BUTTON = (By.ID, 'hubAdd')
    MENU_BUTTON = (By.ID, 'menuDrawer')
    ADD_HUB_BUTTON_MENU = (By.ID, 'addHub')
    SETTINGS_BUTTON_MENU = (By.ID, 'settings')
    HELP_BUTTON_MENU = (By.ID, 'help')
    REPORT_PROBLEM_BUTTON_MENU = (By.ID, 'logs')
    CAMERA_BUTTON_MENU = (By.ID, 'camera')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_menu_button(self):
        self.click_element(DevicesPage.MENU_BUTTON)
