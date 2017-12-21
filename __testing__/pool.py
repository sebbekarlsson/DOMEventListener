from domeventlistener.listen import Listener
from domeventlistener.pool import ListenPool


# my event handler
def event_handler(event_type, data):
    print(event_type, data)


listener0 = Listener(
    domain='https://github.com/sebbekarlsson',
    query='a[title="Stars"]',
    event_handler=event_handler
)

pool = ListenPool()

res = pool.deploy_listener(listener0)
