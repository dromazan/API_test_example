from pytest_example.Resources.resources import base_url
from logging import getLogger, error
import requests


def test_connection():
    # getLogger('connection')
    response = requests.get(base_url)

    # check if response status is 200
    assert response.status_code == 200, 'Response code is not 200'
