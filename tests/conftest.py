"""
Test Fixtures
"""

# import os
import pytest
from app import create_app

@pytest.fixture
def app():
    """App fixture to call the factory method to initialize flask app"""
    app = create_app()

    yield app

@pytest.fixture
def client(app):
    """
    The client fixture calls app.test_client() with the application object
    created by the app fixture. Tests will use the client to make requests
    to the application without running the server.
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    The runner fixture is similar to client. app.test_cli_runner() creates
    a runner that can call the Click commands registered with the application.
    """
    return app.test_cli_runner()
