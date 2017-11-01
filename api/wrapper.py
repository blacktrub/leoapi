import logging
import requests
from typing import Dict, AnyStr, List

from .constants import RequestMethod, LeoPath, BASE_URL
from .settings import EMAIL, PASSWORD


logger = logging.getLogger(__name__)


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
        data = {'email': self.email, 'password': self.password}
        return self.request(
            path=LeoPath.LOGIN,
            method=RequestMethod.POST,
            data=data,
        )

    def translate(self, word: AnyStr) -> List:
        response = self.request(
            path=LeoPath.TRANSLATE,
            method=RequestMethod.GET,
            params={'word': word},
        )
        return [item['value'] for item in response['translate']]

    def send_word(self, word: AnyStr, translate: AnyStr) -> Dict:
        return self.request(
            path=LeoPath.ADDWORD,
            method=RequestMethod.POST,
            data={'word': word, 'tword': translate},
        )

    def request(self,
                path: LeoPath,
                method: RequestMethod,
                **kwargs) -> Dict:
        url = BASE_URL + path.value
        try:
            logger.debug(
                'send request with params: path: %s, method: %s, data: %s',
                path,
                method,
                kwargs.get('params') or kwargs.get('data'),
            )

            response = self.session.request(
                method=method.value,
                url=url,
                **kwargs
            )
        except Exception:
            logger.error('error request', exc_info=True)
        else:
            return response.json()
