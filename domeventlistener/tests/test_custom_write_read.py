from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0
import json
import os


DB_PATH = '/tmp/domeventlistener.db.json'


def read_element():
    db = {}

    if os.path.isfile(DB_PATH):
        with open(DB_PATH) as _file:
            db = json.loads(_file.read())
        _file.close()

    if 'element_str' not in db:
        return None

    return db['element_str']


def write_element(element_str):
    db_contents = ''

    if os.path.isfile(DB_PATH):
        with open(DB_PATH) as _file:
            db_contents = _file.read()
        _file.close()

    db_contents = '{}' if not db_contents else db_contents

    db = json.loads(db_contents)

    db['element_str'] = element_str

    with open(DB_PATH, 'w+') as _file:
        _file.write(json.dumps(db))
    _file.close()

    return db


def test_element_found_on_init():
    listener = Listener(
        document=TEST_DOCUMENT_0,
        query='#the-element',
        read_element=read_element,
        write_element=write_element
    )

    assert listener.read_element_str() is not None

    changed, element = listener.poll_change()

    assert changed is False
    assert element is not None
