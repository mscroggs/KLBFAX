import Queue


class CleanExit(object):
    pass


class InterruptStandardLoop(object):
    pass


class ShowPage(object):
    def __init__(self, page_num):
        self.page_num = page_num


class ShowGreetingPage(object):
    def __init__(self, barcode):
        self.barcode = barcode


queue = Queue.Queue()
