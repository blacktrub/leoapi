EMAIL = 'your@mail.com'
PASSWORD = 'password'

try:
    from .secrets import *
except ModuleNotFoundError:
    pass
