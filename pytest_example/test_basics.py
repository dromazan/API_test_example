from pytest_example.Resources.resources import base_url
from logging import getLogger, error
from urllib import request


def test_connection():
    getLogger('connection')
    req = request.urlopen(base_url)

    # check if response status is 200
    assert req.code == 200

