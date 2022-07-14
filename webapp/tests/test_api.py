from main.api import app


class TestApi:

    def test_get_fruits(self, mocker):
        app.config['TESTING'] = True
        client = app.test_client()

        ret = [{'id': 'FID001'}]
        mocker.patch('main.api.database.find_fruits', return_value=ret)

        result = client.get('/fruits')
        body = result.get_json()

        assert 'OK' == body['result']
        assert ret == body['fruits']
