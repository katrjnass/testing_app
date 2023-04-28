from tests.login.execute_login import execute_login


def test_user_login(user_login_fixture, home_page_fixture, devices_page_fixture, logger_fixture):
    USER_LOGIN = 'qa.ajax.app.automation@gmail.com'
    USER_PASSWORD = 'qa_automation_password'

    logger_fixture.info('Start test_user_login')
    logger_fixture.info('Execute login function')
    execute_login(user_login_fixture, home_page_fixture, logger_fixture, USER_LOGIN, USER_PASSWORD)
    logger_fixture.info('Click login button')
    user_login_fixture.click_on_login_button()
    logger_fixture.info('Check if the user is log in')
    assert devices_page_fixture.find_element(devices_page_fixture.ADD_HUB_BUTTON).is_displayed()
    logger_fixture.info('End test_user_login\n')
