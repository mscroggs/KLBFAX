import zope.event
from threading import Thread
import select
import sys

_subscribers = []


def emit_input_event(arg):
    zope.event.notify(arg)


def subscribe(f):
    zope.event.subscribers.append(f)


def save_subscribers():
    global _subscribers
    _subscribers = zope.event.subscribers[:]


def clear_subscribers():
    del zope.event.subscribers
    zope.event.subscribers = []


def restore_subscribers():
    del zope.event.subscribers
    zope.event.subscribers = _subscribers


def _threaded_function():
    while True:
        input_fd, _, _ = select.select([sys.stdin], [], [])

        if(input_fd):
            input = sys.stdin.readline().strip()
            emit_input_event(input)


is_thread_active = True


def start_keyboard_thread():
    thread = Thread(target=_threaded_function)
    thread.daemon = True
    thread.start()
