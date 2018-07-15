from pytest_example.Resources.resources import base_url, db_path
from pytest_example.Helpers.db_connect import connect_db
from logging import getLogger, error
from urllib import request
from urllib.parse import urlencode
from flata import Query, where
import requests

dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])


def test_posts_POST():
    new_post = {
        "id": '2',
        "title": "new post",
        "author": "me"
    }

    response = requests.post(base_url + '/posts', data=new_post)

    # check if response status is 201
    assert response.status_code == 201, 'response code is not 201. Record is not created'
    assert new_post == response.json(), 'data in request doesn\'t match with response'


def test_posts_PUT():
    new_post = {
        "title": "new post 2",
        "author": "me and me again"
    }

    response = requests.put(base_url + '/posts/2', data=new_post)

    # check if response status is 200
    assert response.status_code == 200, 'response code is not 200'
    # check if modified record matches with request data
    assert new_post == dictfilt(response.json(), new_post.keys()), 'data in request doesn\'t match with response'


def test_posts_GET():

    response = requests.get(base_url + '/posts/2')

    # check if response status is 200
    assert response.status_code == 200, 'response code is not 200'


def test_posts_DELETE():

    response = requests.delete(base_url + '/posts/2')

    # check if response status is 200
    assert response.status_code == 200, 'response code is not 200'
