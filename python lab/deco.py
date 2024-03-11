class Event():
    events = {}

    def add_event(str):
        def wrapper(func):
            print("add event", str)
            if str in Event.events:
                Event.events[str].append(func)
            else:
                Event.events[str] = [func]
            return func
        return wrapper
    
    def call(str):
        if str in Event.events:
            for func in Event.events[str]:
                print("call", func.__name__)
                func()
        else:
            raise f"{str} is not set event"

@Event.add_event("p1")
def func_p1_1():
    print("hello p1 1")
@Event.add_event("p1")
def func_p1_2():
    print("hello p1 2")
@Event.add_event("p2")
def func_p2_1():
    print("hello p2 1")

Event.call("p1")

        
        