class TestLogIn:

    def test_login(self, starting_page):
        login_page = starting_page.go_to_login()
        login_page.log_in_user(username='', password='')
