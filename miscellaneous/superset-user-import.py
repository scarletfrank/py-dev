import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment

class UseSupersetApi:
    def __init__(self, username=None, password=None):
        self.s = requests.Session()
        self.base_url = "http://127.0.0.1:8088/"
        self._csrf = self._getCSRF(self.url('login/'))
        self.headers = {'X-CSRFToken': self._csrf, 'Referer': self.url('login/')}
        # note: does not use headers because of flask_wtf.csrf.validate_csrf
        # if data is dict it is used as form and ends up empty but flask_wtf checks if data ...
        self.s.post(self.url('login/'),
        data={'username': username, 'password': password, 'csrf_token': self._csrf})
        
    def url(self, url_path):
        return self.base_url + url_path

    def get(self, url_path):
        return self.s.get(self.url(url_path), headers=self.headers)

    def post(self, url_path, data=None, json_data=None, **kwargs):
        kwargs.update({'url': self.url(url_path), 'headers': self.headers})
        if data:
            data['csrf_token'] = self._csrf
            kwargs['data'] = data
        if json_data:
            kwargs['json'] = json_data
        return self.s.post(**kwargs)

    def _getCSRF(self, url_path):
        response = self.s.get(self.base_url)
        soup = bs(response.content, "html.parser")
        for tag in soup.find_all('input', id='csrf_token'):
            csrf_token = tag['value']
        return csrf_token

superset = UseSupersetApi('scarlet', 'scar1et')
users = [{
    'first_name': 'fname',
    'last_name':'lname',
    'username': 'cplc',
    'email': 'cplc@gdpost.com',
    'password': 'cplcapp',
    'conf_password': 'cplcapp',
    'roles': ['2', '4', '6']},
    {
    'first_name': 'fn',
    'last_name':'ln',
    'username': 'cplc1',
    'email': 'cplc1@gdpost.com',
    'password': 'cplcapp',
    'conf_password': 'cplcapp',
    'roles': ['2', '6']},
    {
    'first_name': 'fn',
    'last_name':'ln',
    'username': 'cplc2',
    'email': 'cplc2@gdpost.com',
    'password': 'cplcapp',
    'conf_password': 'cplcapp',
    'roles': ['2']}
    ]#some user dicts inside

for user in users:
    payload = {'first_name': user['first_name'],
               'last_name': user['last_name'],
               'username': user['username'],
               'email': user['email'],
               'active': True,
               'conf_password': user['password'],
               'password': user['password'],
               'roles': user['roles']
               } 
    print(superset.post(url_path='users/add', json=payload))