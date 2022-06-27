"""
Testing Admin Blueprint
"""

import pytest

def test_admin_dashboard(client, app):
    """Test that we can load the admin dashboard."""
    response = client.get('/admin/')
    assert response.status_code == 200
    assert b'Admin Dashboard' in response.data
