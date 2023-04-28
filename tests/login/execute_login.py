def execute_login(user_login_fixture, home_page_fixture, logger_fixture, user_login, user_password):

    logger_fixture.info('Click on button authorize')
    home_page_fixture.click_on_button_login()
    logger_fixture.info('Fill email field')
    user_login_fixture.enter_email(user_login)
    logger_fixture.info('Fill password field')
    user_login_fixture.enter_password(user_password)
