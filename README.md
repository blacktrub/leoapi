# Simple LinguaLeo api wrapper

### For start:
1. Clone this project
2. Create a virtual environment
    
    `$ pipenv --three`
3. Install requirements

    `$ pipenv install`

You can to learn more about **pipenv** on [official github page](https://github.com/kennethreitz/pipenv)
### Simple usage:
```python
In [1]: from api import LinguaLeoApi

In [2]: api = LinguaLeoApi(email='your@mail.com', password='yourpassword')

In [3]: api.translate(word='word')
Out[3]: ['слово', 'сообщение', 'речь', 'разговор', 'обещание']

In [4]: api.send_word(word='word', translate='слово')
```

## Enjoy!