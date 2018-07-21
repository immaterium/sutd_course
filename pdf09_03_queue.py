class Queue:

    def __init__(self):
        self._queue = []

    def put(self, item):
        self._queue.append(item)

    def get(self):
        return self._queue.pop(0)

    def qsize(self):
        return len(self._queue)

    def empty(self):
        return self.qsize() == 0   

    