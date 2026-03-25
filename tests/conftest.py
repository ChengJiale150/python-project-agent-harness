import pytest
from typing import Generator


@pytest.fixture(scope="session")
def session_fixture() -> Generator[None, None, None]:
    """Example session-scoped fixture."""
    # Setup
    yield
    # Teardown
