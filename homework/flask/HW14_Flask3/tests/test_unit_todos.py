import pytest
from .conftest import client


def test_get_todos(client):
    response = client.get('/api/v1/todos')
    assert response.status_code == 200
    assert response.json == []


def test_post_todos(client):
    response = client.post('/api/v1/todos', json={'title': 'test1', 'text': 'test text'})
    assert response.status_code == 200


def test_post_todos_complex(client):
    item1 = {'title': 'test1', 'text': 'test text'}
    item2 = {'title': 'test2', 'text': 'test text 2'}
    client.post('/api/v1/todos', json=item2)
    response = client.get('/api/v1/todos')
    assert response.status_code == 200
    assert response.json == [item1, item2]


def test_patch_todos(client):
    client.post('/api/v1/todos', json={'title': 'test1', 'text': 'test text'})
    response = client.patch('/api/v1/todos/0', json={'title': 'test2', 'text': 'test text2'})
    assert response.status_code == 200


def test_del_todos(client):
    client.post('/api/v1/todos', json={'title': 'test1', 'text': 'test text'})
    response = client.delete('/api/v1/todos/0')
    assert response.status_code == 200
