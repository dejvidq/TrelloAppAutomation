import random
import string

import pytest


class TestBoards:

    @pytest.mark.usefixtures("delete_all_boards_after_test")
    def test_add_board(self, starting_page, user):
        username, password = user
        board_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        login_page = starting_page.go_to_login()
        main_page = login_page.log_in_user(username=username, password=password)
        board_page = main_page.add_board(board_name=board_name)
        assert board_page.is_board_created(board_name=board_name)
