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

    @pytest.mark.usefixtures("delete_all_boards_after_test")
    def test_add_multiple_boards(self, starting_page, user):
        username, password = user
        login_page = starting_page.go_to_login()
        main_page = login_page.log_in_user(username=username, password=password)
        board_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        board_page = main_page.add_board(board_name=board_name)
        assert board_page.is_board_created(board_name=board_name)
        main_page = board_page.go_back_to_main_boards_page()
        board_name_2 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        board_page = main_page.add_board(board_name=board_name_2)
        assert board_page.is_board_created(board_name=board_name_2)
        main_page = board_page.go_back_to_main_boards_page()
        board_name_3 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        board_page = main_page.add_board(board_name=board_name_3)
        assert board_page.is_board_created(board_name=board_name_3)
        main_page = board_page.go_back_to_main_boards_page()
        assert main_page.is_board_visible(board_name=board_name)
        assert main_page.is_board_visible(board_name=board_name_2)
        assert main_page.is_board_visible(board_name=board_name_3)
