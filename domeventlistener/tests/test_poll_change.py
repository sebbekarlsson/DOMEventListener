from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0, get_ugly_htmls
from bs4 import BeautifulSoup


CSS_QUERY = '#the-element'


def test_poll_change_not_changed():
    listener = Listener(
        document_path=TEST_DOCUMENT_0,
        query=CSS_QUERY
    )

    listener.mount()

    has_changed, element = listener.poll_change()

    assert has_changed is False
    assert element is not None


def test_poll_change_changed():
    listener = Listener(
        document_path=TEST_DOCUMENT_0,
        query=CSS_QUERY
    )

    listener.mount()

    has_changed, element = listener.poll_change()

    assert has_changed is False
    assert element is not None

    htmlcontent = ''
    with open(TEST_DOCUMENT_0) as _file:
        htmlcontent = _file.read()
    _file.close()

    soup = BeautifulSoup(htmlcontent, 'html.parser')
    soup_elem = soup.select('#the-element')[0]

    soup_elem['data-changed'] = 1

    with open(TEST_DOCUMENT_0, 'w') as\
            _file:
        _file.write(str(soup))
    _file.close()

    has_changed, element = listener.poll_change()
    assert has_changed is True

    # write back old data to mock file
    htmlcontent = ''
    with open(TEST_DOCUMENT_0) as _file:
        htmlcontent = _file.read()
    _file.close()

    soup = BeautifulSoup(htmlcontent, 'html.parser')
    soup_elem = soup.select('#the-element')[0]

    del soup_elem['data-changed']

    with open(TEST_DOCUMENT_0, 'w') as\
            _file:
        _file.write(str(soup))
    _file.close()


def test_poll_ugly_elements():
    ugly_htmls = list(get_ugly_htmls())
    index = 0

    listener = Listener(
        document=ugly_htmls[index],
        query='#the-element'
    )
    listener.mount()
    index += 1

    for i in range(index, len(ugly_htmls)):
        listener.document = ugly_htmls[i]
        has_changed, element = listener.poll_change()

        assert has_changed is True
