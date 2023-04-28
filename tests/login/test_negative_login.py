import pytest

from tests.login.execute_login import execute_login


@pytest.mark.parametrize('email, password', [
    ('qa.ajax.app.automation@gmail.com', ''),
    ('', 'qa_automation_password'),
    ('non_valid_format_email', 'qa_automation_password'),
    ('qa.ajax.app.automation@gmail.com', 'non_valid_password'),
    ('non_valid_email@gmail.com', 'qa_automation_password')
])
def test_negative_login(user_login_fixture, home_page_fixture, logger_fixture, email, password):
    list_non_valid_messages = ['Неверный логин или пароль', 'Неверный формат электронной почты']

    logger_fixture.info(f'Start test_negative_login with email: \'{email}\' and password: \'{password}\'')
    logger_fixture.info('Execute login function')
    execute_login(user_login_fixture, home_page_fixture, logger_fixture, email, password)
    logger_fixture.info('Check if the button is clickable')

    login_button_clickable = user_login_fixture.find_element(user_login_fixture.LOGIN_BUTTON_VIEW).is_enabled()
    if login_button_clickable:
        user_login_fixture.click_on_login_button()
        assert user_login_fixture.find_element(user_login_fixture.ALERT_NON_VALID_DATA).text in list_non_valid_messages
    else:
        assert not login_button_clickable
    logger_fixture.info('End test_negative_login\n')
