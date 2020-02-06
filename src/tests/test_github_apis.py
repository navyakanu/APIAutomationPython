import requests
import pytest
import json
import models.users
import jsonpickle

class TestClass:

    def test_for_get_request(self):
        response = requests.get('https://api.github.com/search/users?q=twqablore')
        assert(response.status_code == 200)
        print(response.json())
        assert(response.json().get('items')[0].get('avatar_url') == 'https://avatars1.githubusercontent.com/u/17001476?v=4')

    def test_for_reqres_requests(self):
        response = requests.get('https://reqres.in/api/users/2')
        expected_data_from_model = models.users.Data(2,
                                     'janet.weaver@reqres.in',
                                     'Janet',
                                     'Weaver',
                             'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg')

        expected_response = json.loads(jsonpickle.encode(expected_data_from_model,unpicklable=False))
        actual_response = response.json()
        print(type(actual_response))
        print(type(expected_response))
        assert(expected_response == actual_response)
        assert(expected_response.get('data').get('id') == actual_response.get('data').get('id'))
        assert(response.status_code == 500)

