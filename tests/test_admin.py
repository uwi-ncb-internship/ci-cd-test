"""
Testing Admin Blueprint
"""

import pytest

def test_admin_dashboard(client, app):
    """Test that we can load the admin dashboard."""
    assert client.get('/admin').status_code == 200
