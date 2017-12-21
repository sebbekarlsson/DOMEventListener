from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0


def test_element_found_on_init():
    listener = Listener(
        document=TEST_DOCUMENT_0,
        query='#the-element'
    )

    assert listener.element_str is not None
