import pytest
from {project}.main import hello

@pytest.mark.unit
def test_hello_default():
    assert hello() == "Hello, World!"

@pytest.mark.unit
def test_hello_with_name():
    assert hello("Python") == "Hello, Python!"
