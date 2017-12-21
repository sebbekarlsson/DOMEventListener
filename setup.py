from setuptools import setup


setup(
    name='DOMEventListener',
    version='1.6',
    description='Subscripe on DOM elements, trigger methods when they change',
    url='https://github.com/sebbekarlsson/DOMEventListener',
    install_requires=[
        'requests',
        'bs4',
        'selenium==3.0.0',
        'pyvirtualdisplay==0.2.1'
    ],
    packages=[
        'domeventlistener'
    ],
    entry_points={
        "console_scripts": [
            "domeventlistener = domeventlistener.bin:run"
        ]
    }
)
