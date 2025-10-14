class EventBus:
    def __init__(self):
        self._subscribers = []                    		 # list of subscriber callables

    def subscribe(self, fn):
        self._subscribers.append(fn)               		# register a subscriber function

    def publish(self, event):
        for fn in self._subscribers:
            fn(event)                              			# notify each subscriber with the event

def on_start(event):
    print("Started:", event)                       		# subscriber function example

bus = EventBus()
bus.subscribe(on_start)                           		# subscribe
bus.publish({"vehicle": "Car", "action": "start"})  	# publish event
