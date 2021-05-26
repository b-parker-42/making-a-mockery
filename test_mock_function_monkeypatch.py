import requests

from mock_function import get_todo_from_id

# Any arguments may be passed and mock_get() will always return our
# mocked object, which only has the .json() method.
def mock_get(*args, **kwargs):
    return MockResponse()


def test_get_todo_from_id_success(monkeypatch):
    # custom class to be the mock return value
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
        def json(self):
            return {
        'userId': 1,
        'id': 1,
        'title': 'some Latin words',
        'completed': False
    }
    
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()
        
    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = get_todo_from_id(1)
    assert result["userId"] == 1
    assert result["id"] == 1

def test_get_todo_from_id_fail(monkeypatch):
    # custom class to be the mock return value
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
        def json(self):
            # Returns empty json if the id doesn't exist
            return {}

    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = get_todo_from_id('hi')
    assert result == {}