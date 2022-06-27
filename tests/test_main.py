"""
Testing Main Blueprint
"""
import pytest

def test_index(client, app):
    """Test that we can load the index page."""
    assert client.get('/').status_code == 200
