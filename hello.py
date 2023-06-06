class Queue:
    def __init__(self):
        self.items = []
    def dequeue(self):
        return self.items.pop(0)
    def enqueue(self, item):
        self.items.append(item)
    def is_empty(self):
        return self.items == []
    def see(self):
        return self.items

queue = Queue()
queue.enqueue(0)
print(queue.dequeue())
print(queue.see())