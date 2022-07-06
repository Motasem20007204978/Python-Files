
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

import queue


class Queue:
    def __init__(self):
        self.queue = queue.Queue()

    def isEmpty(self):
        return self.qfueue.empty()

    def enqueue(self, item):
        self.queue.put(item)

    def dequeue(self):
        return self.queue.get()

    def size(self):
        return self.queue.qsize()

    def front(self):
        return self.queue.queue[0]

    def rear(self):
        return self.queue.queue[-1]


