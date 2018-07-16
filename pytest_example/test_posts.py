from pytest_example.Resources.resources import base_url, db_path
from pytest_example.Helpers.db_connect import *
import requests
import time

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
    # check if response matches with request
    assert new_post == response.json(), 'data in request doesn\'t match with response'
    time.sleep(1)  # required for data to be added to DB
    # check if data is added to DB and matches with request
    assert find_post(connect_db(), new_post), 'data in DB doesn\'t match with requested data'

def test_posts_PUT():
    new_post = {
        "title": "new post 3",
        "author": "me and me again"
    }

    response = requests.put(base_url + '/posts/2', data=new_post)

    # check if response status is 200
    assert response.status_code == 200, 'response code is not 200'
    # check if modified record matches with request data
    assert new_post == dictfilt(response.json(), new_post.keys()), 'data in request doesn\'t match with response'
    time.sleep(1)  # required for data to be added to DB
    # check if data is added to DB and matches with request
    assert find_post_by_id(connect_db(), '2') == response.json(), 'data in DB doesn\'t match with requested data'


def test_posts_GET():

    response = requests.get(base_url + '/posts/2')

    # check if response status is 200
    assert response.status_code == 200, 'response code is not 200'
    time.sleep(1)  # required for data to be added to DB
    # check if data is received from the DB and matches with response
    assert find_post_by_id(connect_db(), '2') == response.json(), 'data in DB doesn\'t match with requested data'


def test_posts_DELETE():

    response = requests.delete(base_url + '/posts/2')

    # check if response status is 200
    assert response.status_code == 200, 'response code is not 200'
    assert response.json() == {}, 'response body is not empty'
    time.sleep(1)
    # required for data to be added to DB
    # check if data is deleted from the DB
    assert find_post_by_id(connect_db(), '2') == ValueError, 'data in DB doesn\'t match with requested data'