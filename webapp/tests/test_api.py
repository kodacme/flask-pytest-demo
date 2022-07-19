import pytest

from main.api import app


@pytest.fixture(scope='class')
def test_app():
    app.config['TESTING'] = True
    return app.test_client()


class TestApi:

    def test_get_fruits(self, test_app, mocker):

        ret = [{'id': 'FID001'}]
        mocker.patch('main.api.database.find_fruits', return_value=ret)

        result = test_app.get('/fruits')
        body = result.get_json()

        assert 'OK' == body['result']
        assert ret == body['fruits']

    def test_get_fruits_failure(self, test_app, mocker):
        ret = [{'id': 'FID002'}]
        mocker.patch('main.api.database.find_fruits', return_value=ret)

        result = test_app.get('/fruits')
        body = result.get_json()

        assert 'OK' == body['result']
        assert ret == body['fruits']
