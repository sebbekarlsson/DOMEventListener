from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0


def test_read_element():
    listener = Listener(
        document=TEST_DOCUMENT_0,
        query='#the-element'
    )

    listener.find_element()

    assert isinstance(listener.read_element_str(), basestring)
