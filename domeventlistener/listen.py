# -*- coding: utf-8 -*-
from requests import Session
from bs4 import BeautifulSoup
import time
from domeventlistener.utils import unidiff_output
import threading


EVENT_CHANGED = 'changed'
EVENT_EMPTIED = 'emptied'


class Listener(threading.Thread):

    def __init__(
        self,
        domain=None,
        query=None,
        event_handler=None,
        document_path=None,
        document=None,
        read_element=None,
        write_element=None,
        chrome=None,
        daemon=True
    ):
        self.domain = domain
        self.query = query
        self.event_handler = event_handler
        self.document_path = document_path
        self.document = document
        self.read_element = read_element
        self.write_element = write_element
        self.session = Session()
        self.chrome = chrome
        self.element_str = None

    def mount(self):
        return self.write_element_str(str(self.find_element()))

    def find_element(self):
        if self.document_path:
            with open(self.document_path) as _file:
                htmlcontent = _file.read()
            _file.close()
        elif self.document:
            htmlcontent = self.document
        elif self.chrome:
            self.chrome.get(self.domain)

            try:
                element = self.chrome.find_element_by_xpath(self.query)
            except Exception:
                element = self.chrome.find_element_by_css_selector(self.query)

            return element.get_attribute('outerHTML')
        else:
            resp = self.session.get(self.domain)
            htmlcontent = resp.text

        document = BeautifulSoup(htmlcontent, 'html.parser')
        elements = document.select(self.query)

        return elements[0] if elements else None

    def read_element_str(self):
        ''' fetch stored old element '''

        return self.element_str if not self.read_element\
            else self.read_element()

    def write_element_str(self, element_str):
        ''' write to store '''

        if not self.write_element:
            self.element_str = str(element_str)
        else:
            self.write_element(element_str)

    def poll_change(self):
        ''' Returns a tuple (has_changed, new_element_str) '''

        new_element = self.find_element()
        old_element = self.read_element_str()

        try:
            new_element = new_element.encode('utf-8', 'ignore')
        except UnicodeDecodeError:
            new_element = new_element.decode('utf-8').encode('utf-8', 'ignore')

        try:
            old_element = old_element.encode('utf-8', 'ignore')
        except UnicodeDecodeError:
            old_element = old_element.decode('utf-8').encode('utf-8', 'ignore')

        changed = new_element != old_element

        return changed, new_element

    def run(self, sleep_time=5):
        while True:
            has_changed, new_element_str = self.poll_change()

            if has_changed:
                self.event_handler(
                    EVENT_CHANGED if new_element_str else EVENT_EMPTIED,
                    unidiff_output(
                        self.read_element_str(),
                        new_element_str
                    )
                ) if self.event_handler else None

                self.write_element_str(new_element_str)
                time.sleep(sleep_time)
