import requests
import config


def get_request_data(api_url: str = config.BASE_API_URL, endpoint: str = ""):
    path = api_url + endpoint
    data = requests.get(path)
    return data.json()
