# -*- coding: utf-8 -*-
import json


DB_PATH = '/tmp/domeventlistener.db.json'
TEST_DOCUMENT_0 = 'domeventlistener/tests/mock/test_document_0.html'
NAUGHTY_STRINGS = []

with open('domeventlistener/tests/mock/blns.base64.json') as _file:
    NAUGHTY_STRINGS = json.loads(_file.read())
_file.close()


def get_ugly_htmls():
    for ugly_string in NAUGHTY_STRINGS:
        yield """
        <html>
            <body>
                <div id="the-element">
                {}
                </div>
            </body>
        </html>
        """.format(ugly_string)
