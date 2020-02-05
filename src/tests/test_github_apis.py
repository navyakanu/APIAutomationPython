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

    @pytest.mark.wip
    def test_for_reqres_requests(self):
        response = requests.get('https://reqres.in/api/users/2')
        assert(response.status_code == 200)
        expected_data = jsonpickle.encode(models.users.Data(2,
                                     'janet.weaver@reqres.in',
                                     'Janet',
                                     'Weaver',
                             'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg').__dict__)
        print(type(expected_data))

        #assert(jsonpickle.decode(response.text == expected_data))
        assert(response.status_code == 200)
#         assert(response.json().get('data').get('id') == 1)

