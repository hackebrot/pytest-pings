import pytest


class Server:
    """Telemetry ping server."""


@pytest.fixture
def server():
    return Server()

