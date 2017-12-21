# -*- coding: utf-8 -*-
from domeventlistener.listen import Listener
import sys


URL = sys.argv[1]
QUERY = sys.argv[2]


# my event handler
def event_handler(event_type, data):
    print('{} | {}, {}'.format(QUERY, event_type, data.encode('utf-8')))


listener = Listener(
    URL,
    QUERY,
    event_handler
)

listener.mount()


def run():
    try:
        listener.start()
    except KeyboardInterrupt():
        quit()
