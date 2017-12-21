from domeventlistener.tests.mock import DB_PATH
import pytest
import os


def initializer():
    os.remove(DB_PATH)


@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    request.addfinalizer(initializer)
