import requests


class API:

    def __init__(self, key: str, token: str):
        self.key = key
        self.token = token
        self.base_url = "https://api.trello.com/1{}?key=" + self.key + "&token=" + self.token

    def get_all_boards(self):
        url = "/members/me/boards"
        resp = requests.get(self.base_url.format(url))
        return resp.json()

    def get_board(self, board_name):
        boards = self.get_all_boards()
        for board in boards:
            if board['name'] == board_name:
                return board

    def delete_board(self, board_name):
        board = self.get_board(board_name=board_name)
        board_id = board['id']
        url = self.base_url.format(f"/boards/{board_id}")
        resp = requests.delete(url)
        return resp.json()

    def delete_all_boards(self):
        boards = self.get_all_boards()
        for board in boards:
            self.delete_board(board_name=board['name'])
