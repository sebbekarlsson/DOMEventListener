# DOMEventListener
> Subscripe on DOM elements, trigger methods when they change


## Usage
> Example: _Subscribing on the stackoverflow feed_:

    from domeventlistener.listen import Listener


    # your event handler
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

> For example, when the DOM has changed the `event_handler` defined will print  
> something like:

    'changed', <unified diff between the new data and the old>
