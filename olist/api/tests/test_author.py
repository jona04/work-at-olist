import pytest
from rest_framework.test import RequestsClient


@pytest.fixture
def resp(client):
    return client.get('/')


def test_name_author(resp):
    client = RequestsClient()
    response = client.get('http://localhost:8000')
    assert response.status_code == 200
