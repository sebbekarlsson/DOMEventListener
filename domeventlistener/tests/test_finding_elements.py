from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0


def test_find_element():
    listener = Listener(
        document=TEST_DOCUMENT_0,
        query='#the-element'
    )

    assert listener.find_element() is not None
