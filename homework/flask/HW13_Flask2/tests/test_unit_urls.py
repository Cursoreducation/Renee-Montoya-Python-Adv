import os


def test_url_root(client):
    key = os.getenv("WEATHER_API_KEY")
    response = client.get('/')
    assert response.status == '200 OK'
    assert key == response.data.decode()


def test_url_display_text(client):
    response = client.get('/display-text')
    assert response.status == '200 OK'
    assert b"<title>Text page</title>" in response.data


def test_urltext_new(client):
    response = client.get('/text/new/')
    assert response.status == '200 OK'
    assert b'<input type="submit">' in response.data


def test_url_save(client):
    response = client.post('/save', data={'text': 'ddsgsdgsdgsd'})
    assert response.status == '302 FOUND'


def test_url_get_weather(client):
    response = client.get('/get-your-weather')
    assert response.status == '200 OK'
    assert b"Timezone" in response.data
