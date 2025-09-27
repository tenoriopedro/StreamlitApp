import requests
from utils.env_path import get_url_api


class Auth:

    def __init__(self):
        self.__base_url = get_url_api()
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )

        if auth_response.status_code == 200:
            return auth_response.json()
        return {
            'error': (
                f'Erro ao autenticar. Status code: {auth_response.status_code}'
            )
        }
