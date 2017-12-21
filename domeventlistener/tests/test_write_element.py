from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0


def test_write_element():
    listener = Listener(
        document=TEST_DOCUMENT_0,
        query='#the-element'
    )

    listener.mount()

    listener.find_element()

    listener.write_element_str(listener.read_element_str())

    assert listener.element_str is not None
