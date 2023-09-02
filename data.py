from requests import session
from fake_useragent import FakeUserAgent
class Data():
    _headers = {
        'user-agent': FakeUserAgent().random
    }
    _session = session()
    _api = 'https://api.fakeyou.com/{}'.format