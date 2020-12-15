import configparser


def parse_config(conf_file):
    config = configparser.ConfigParser()
    config.read(conf_file)
    return config


def parse_rd_config(conf_file) -> dict:
    config = parse_config(conf_file)
    device_name = config.get('RD', 'name', fallback=None)
    appium_ip = config.get('RD', 'appium_ip', fallback=None)
    appium_port = config.get('RD', 'appium_port', fallback=None)
    appium_server_url = f"{appium_ip}:{appium_port}"
    app_package = config.get('RD', 'appPackage', fallback=None)
    app_activity = config.get('RD', 'appActivity', fallback=None)
    udid = config.get('RD', 'udid', fallback=None)
    platform_name = config.get('RD', 'platformName', fallback=None)
    platform_version = config.get('RD', 'platformVersion', fallback=None)
    caps = {
        'appPackage': app_package,
        'appActivity': app_activity,
        'udid': udid,
        'platformName': platform_name,
        'platformVersion': platform_version,
        'deviceName': device_name
    }
    return {'appium_server_url': appium_server_url, 'caps': caps}
