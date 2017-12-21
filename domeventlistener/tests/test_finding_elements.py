from domeventlistener.listen import Listener
from domeventlistener.tests.mock import TEST_DOCUMENT_0, get_ugly_htmls
from domeventlistener.tests.config import config
from selenium.webdriver.chrome.options import Options
#  from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium import webdriver
from pyvirtualdisplay import Display

chrome_options = Options()
chrome_options.add_argument("--headless")

CHROME = None
CHROMEDRIVER_PATH = config['chromedriver'] if 'chromedriver' in config\
    else None

if CHROMEDRIVER_PATH:
    DISPLAY = Display(visible=0, size=(800, 600))
    DISPLAY.start()

    CHROME = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options
    )


def test_find_element():
    listener = Listener(
        document_path=TEST_DOCUMENT_0,
        query='#the-element',
        chrome=CHROME
    )

    listener.mount()

    assert listener.find_element() is not None

    listener = Listener(
        domain='http://example.org/',
        query='h1',
        chrome=CHROME
    )

    listener.mount()

    assert listener.find_element() is not None


def test_find_ugly_elements():
    for html in get_ugly_htmls():
        listener = Listener(
            document=html,
            query='#the-element',
            chrome=CHROME
        )

        listener.mount()

        assert listener.find_element() is not None

    if DISPLAY:
        DISPLAY.stop()

    if CHROME:
        CHROME.quit()
