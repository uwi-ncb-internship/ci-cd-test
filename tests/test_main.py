import pytest

def test_index(client, app):
    assert client.get('/').status_code == 200