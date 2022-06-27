"""
Test Fixtures
"""

import pytest
import os
from app import create_app

@pytest.fixture
def testapp():
    app = create_app()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
