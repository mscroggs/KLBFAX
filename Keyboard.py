import zope.event
from threading import Thread
import select
import sys


def emit_input_event(arg):
    zope.event.notify(arg)


def subscribe(f):
    zope.event.subscribers.append(f)


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

