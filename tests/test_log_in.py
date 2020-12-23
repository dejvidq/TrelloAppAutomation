from utils import get_user


class TestLogInLogOut:

    def test_login(self, starting_page):
        username, password = get_user()
        login_page = starting_page.go_to_login()
        boards_page = login_page.log_in_user(username=username, password=password)
        assert boards_page.is_logged_in()

    def test_log_out(self, starting_page):
        username, password = get_user()
        login_page = starting_page.go_to_login()
        boards_page = login_page.log_in_user(username=username, password=password)
        settings_page = boards_page.open_settings()
        settings_page.log_out()
