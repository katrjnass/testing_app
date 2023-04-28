from tests.login.execute_login import execute_login


def test_sidebar_elements(user_login_fixture, home_page_fixture, devices_page_fixture, logger_fixture):
    USER_LOGIN = 'qa.ajax.app.automation@gmail.com'
    USER_PASSWORD = 'qa_automation_password'
    sidebar_elements = [devices_page_fixture.ADD_HUB_BUTTON_MENU, devices_page_fixture.SETTINGS_BUTTON_MENU,
                        devices_page_fixture.HELP_BUTTON_MENU, devices_page_fixture.REPORT_PROBLEM_BUTTON_MENU,
                        devices_page_fixture.CAMERA_BUTTON_MENU]

    logger_fixture.info('Start test_sidebar_elements')
    logger_fixture.info('Execute login function')
    execute_login(user_login_fixture, home_page_fixture, logger_fixture, USER_LOGIN, USER_PASSWORD)
    logger_fixture.info('Click login button')
    user_login_fixture.click_on_login_button()
    logger_fixture.info('Click on menu button')
    devices_page_fixture.click_on_menu_button()
    for element in sidebar_elements:
        logger_fixture.info(f'Check if {element[1]} button is displayed')
        assert devices_page_fixture.find_element(element).is_displayed()
    logger_fixture.info('End test_sidebar_elements\n')
