from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    LOGIN_TEXT_FIELD = (By.XPATH, '//android.widget.FrameLayout[1]//android.widget.EditText')
    PASSWORD_TEXT_FIELD = (By.XPATH, '//android.widget.FrameLayout[2]//android.widget.EditText')
    LOGIN_BUTTON = (By.ID, 'authLogin')
    # использую потому что на LOGIN_BUTTON элементе кликабельность всегда false
    LOGIN_BUTTON_VIEW = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView[2]//android.view.View/android.view.View')
    ALERT_NON_VALID_DATA = (By.ID, 'snackbar_text')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.input_data(LoginPage.LOGIN_TEXT_FIELD, email)

    def enter_password(self, password):
        self.input_data(LoginPage.PASSWORD_TEXT_FIELD, password)

    def click_on_login_button(self):
        self.click_element(LoginPage.LOGIN_BUTTON)
