from requests import Session
from bs4 import BeautifulSoup
import time
from domeventlistener.utils import unidiff_output


EVENT_CHANGED = 'changed'


class Listener(object):

    def __init__(self, domain, query, event_handler):
        self.domain = domain
        self.query = query
        self.event_handler = event_handler
        self.session = Session()
        self.element = None

    def on_event(self, event_type, data):
        return self.event_handler(event_type, data)

    def start(self, sleep_time=5):
        while True:
            resp = self.session.get(self.domain)
            document = BeautifulSoup(resp.text, 'html.parser')
            _element = document.select(self.query)

            if str(_element) != str(self.element):
                self.on_event(
                    EVENT_CHANGED,
                    unidiff_output(str(self.element), str(_element))
                )

            self.element = _element

            time.sleep(sleep_time)
