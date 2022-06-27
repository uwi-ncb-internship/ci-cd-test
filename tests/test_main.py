"""
Testing Main Blueprint
"""

# import pytest

def test_index(client):
    """Test that we can load the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Main Website' in response.data
