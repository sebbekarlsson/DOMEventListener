from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0, get_ugly_htmls


def test_find_element():
    listener = Listener(
        document_path=TEST_DOCUMENT_0,
        query='#the-element'
    )

    listener.mount()

    assert listener.find_element() is not None

    listener = Listener(
        domain='http://example.org/',
        query='h1'
    )

    listener.mount()

    assert listener.find_element() is not None


def test_find_ugly_elements():
    for html in get_ugly_htmls():
        listener = Listener(
            document=html,
            query='#the-element'
        )

        listener.mount()

        assert listener.find_element() is not None
