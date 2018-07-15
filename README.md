# API_test_example

## Install JSON Server:

npm install -g json-server

## Start JSON Server:

json-server --watch db.json


### https://github.com/typicode/json-server

## Run tests:

python -m pytest -v

## Result:
```
============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.6.3, py-1.5.4, pluggy-0.6.0 -- C:\Users\droma\PycharmProjects\API_test\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\droma\PycharmProjects\API_test, inifile:
plugins: tavern-0.14.4
collected 11 items

pytest_example/test_basics.py::test_connection PASSED                    [  9%]
pytest_example/test_posts.py::test_posts_POST PASSED                     [ 18%]
pytest_example/test_posts.py::test_posts_PUT PASSED                      [ 27%]
pytest_example/test_posts.py::test_posts_GET PASSED                      [ 36%]
pytest_example/test_posts.py::test_posts_DELETE PASSED                   [ 45%]
tavern_example/test_basics.tavern.yaml::Make sure server api is running PASSED [ 54%]
tavern_example/test_posts.tavern.yaml::GET first post PASSED             [ 63%]
tavern_example/test_posts.tavern.yaml::POST new post PASSED              [ 72%]
tavern_example/test_posts.tavern.yaml::Update existing post with PUT PASSED [ 81%]
tavern_example/test_posts.tavern.yaml::Update existing post with PATCH PASSED [ 90%]
tavern_example/test_posts.tavern.yaml::Delete post PASSED                [100%]

========================= 11 passed in 13.44 seconds ==========================

```