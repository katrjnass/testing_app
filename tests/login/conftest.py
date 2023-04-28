import pytest

from framework.login_page import LoginPage
from framework.home_page import HomePage
from framework.devices_page import DevicesPage


@pytest.fixture(scope='function')
def user_login_fixture(driver, change_activity_app_fixture):
    yield LoginPage(driver)


@pytest.fixture(scope='function')
def home_page_fixture(driver, change_activity_app_fixture):
    yield HomePage(driver)


@pytest.fixture(scope='function')
def devices_page_fixture(driver, change_activity_app_fixture):
    yield DevicesPage(driver)
