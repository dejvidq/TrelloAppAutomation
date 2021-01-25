import requests


class API:

    def __init__(self, key: str, token: str):
        self.key = key
        self.token = token
        self.base_url = "https://api.trello.com/1{}?key=" + self.key + "&token=" + self.token

    def get_all_boards(self) -> dict:
        url = "/members/me/boards"
        resp = requests.get(url=self.base_url.format(url))
        return resp.json()

    def get_board(self, board_name: str) -> dict:
        boards = self.get_all_boards()
        for board in boards:
            if board['name'] == board_name:
                return board

    def delete_board(self, board_name: str) -> dict:
        board = self.get_board(board_name=board_name)
        board_id = board['id']
        url = self.base_url.format(f"/boards/{board_id}")
        resp = requests.delete(url=url)
        return resp.json()

    def delete_all_boards(self) -> None:
        boards = self.get_all_boards()
        for board in boards:
            self.delete_board(board_name=board['name'])

    def create_board(self, board_name: str) -> dict:
        url = self.base_url.format(f"/boards/")
        url += f"&name={board_name}"
        resp = requests.post(url=url)
        return resp.json()
