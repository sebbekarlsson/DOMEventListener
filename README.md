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

### Changing where data is stored
> By default, the element is stored in the `RAM` memory, you can change this  
> by setting read and write functions.

> For example, if you want to use _MongoDB_:

    from domeventlistener.listen import Listener
    from myapp.mongo import db
    
    
    def read_element():
        return db.collections.find_one({'name': 'element'})

    def write_element(element_str):
        return db.collections.update_one(
            {'name': 'element', 'element_str': element_str},
            upsert=True
        )
    
    ...

    listener = Listener(
        'https://stackoverflow.com/questions',
        '#mainbar',
        event_handler,
        read_element=read_element,
        write_element=write_element
    )
    ...
