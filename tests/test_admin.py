"""
Testing Admin Blueprint
"""

import pytest

def test_admin_dashboard(client, app):
    assert client.get('/admin').status_code == 200
