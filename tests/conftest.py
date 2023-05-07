import pytest
from school_system.app import create_app


@pytest.fixture(scope="module")
def app():
    """ Instance of main Flask """
    return create_app()