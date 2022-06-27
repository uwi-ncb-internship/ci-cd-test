"""
Testing Admin Blueprint
"""

# import pytest

def test_admin_dashboard(client):
    """Test that we can load the admin dashboard."""
    response = client.get('/admin/')
    assert response.status_code == 200
    assert b'Admin Dashboard' in response.data

def test_admin_users(client):
    """Test that we can load the admin dashboard."""
    response = client.get('/admin/users')
    assert response.status_code == 200
    assert b'test' in response.data
