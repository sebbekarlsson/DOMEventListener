from domeventlistener.listen import Listener


# my event handler
def event_handler(event_type, data):
    print(event_type, data)


listener = Listener(
    'https://stackoverflow.com/questions',
    '#mainbar',
    event_handler
)

try:
    listener.start()
except KeyboardInterrupt():
    quit()
