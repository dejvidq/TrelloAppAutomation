class TestLogInLogOut:

    def test_login(self, starting_page, user):
        username, password = user
        login_page = starting_page.go_to_login()
        main_page = login_page.log_in_user(username=username, password=password)
        assert main_page.is_logged_in()

    def test_log_out(self, starting_page, user):
        username, password = user
        login_page = starting_page.go_to_login()
        main_page = login_page.log_in_user(username=username, password=password)
        settings_page = main_page.open_settings()
        starting_page = settings_page.log_out()
        assert starting_page.is_user_logged_out()

    def test_log_in_incorrect_password(self, starting_page, user):
        username, password = user
        login_page = starting_page.go_to_login()
        login_page.log_in_user(username=username, password="wrong_password")
        assert login_page.is_wrong_password_error_shown()
