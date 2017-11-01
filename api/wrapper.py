import requests
from typing import Dict, AnyStr, List

from .constants import RequestMethod, BASE_URL
from .settings import EMAIL, PASSWORD


class LinguaLeoApi:
    email = None
    password = None
    session = None

    def __init__(self,
                 email: AnyStr=EMAIL,
                 password: AnyStr=PASSWORD):
        self.email = email
        self.password = password
        self.session = requests.session()

        self.auth()

    def auth(self) -> Dict:
        data = {
            'email': self.email,
            'password': self.password,
        }
        return self.request(
            path='/api/login',
            method=RequestMethod.POST,
            data=data,
        )

    def translate(self, word: AnyStr) -> List:
        response = self.request(
            path='/gettranslates',
            method=RequestMethod.GET,
            params={'word': word},
        )
        return [item['value'] for item in response['translate']]

    def send_word(self, word: AnyStr, translate: AnyStr):
        return self.request(
            path='/addword',
            method=RequestMethod.POST,
            data={'word': word, 'tword': translate},
        )

    def request(self,
                path: AnyStr,
                method: RequestMethod,
                **kwargs) -> Dict:
        url = BASE_URL + path
        response = self.session.request(
            method=method.value,
            url=url,
            **kwargs
        )
        return response.json()
