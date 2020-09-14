import requests


# запрос к API
def get_response(url, username=None, token=None):
    if not username:
        return requests.get(url=url)

    return requests.get(url=url, auth=(username, token))
