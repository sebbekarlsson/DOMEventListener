from setuptools import setup


setup(
    name='DOMEventListener',
    version='1.0',
    install_requires=[
        'requests',
        'bs4'
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
