import subprocess
import time
import pytest

from appium import webdriver
from utils.Logger import Logger
from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server(logger_fixture):
    logger_fixture.info('Start Appium Server')
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure' 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='function')
def change_activity_app_fixture(driver):
    yield
    driver.reset()


@pytest.fixture(scope='session')
def logger_fixture():
    logger = Logger()
    yield logger.get_logger()


@pytest.fixture(scope='session')
def driver(run_appium_server, logger_fixture):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    logger_fixture.info("Start connection")
    yield driver
    logger_fixture.info("Close connection")
    driver.quit()
