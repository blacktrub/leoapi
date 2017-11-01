import enum


BASE_URL = 'http://api.lingualeo.com'


class RequestMethod(enum.Enum):
    GET = 'GET'
    POST = 'POST'

    def __str__(self):
        return self._value_


class LeoPath(enum.Enum):
    LOGIN = '/api/login'
    TRANSLATE = '/gettranslates'
    ADDWORD = '/addword'

    def __str__(self):
        return self._value_
