import pytest
# from model_bakery import baker

def test_the_view_can_list_posts(client) -> None:
    response = client.get('/api/v1/')

    assert response.status_code == 200
