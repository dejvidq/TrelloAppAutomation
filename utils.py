from config_parser import parse_config


def get_user() -> tuple:
    config = parse_config('user.ini')
    username = config.get('User', 'username', fallback=None)
    password = config.get('User', 'password', fallback=None)
    return username, password
