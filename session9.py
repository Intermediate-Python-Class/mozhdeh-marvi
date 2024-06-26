# Queue
# queue functions:
# enqueue
# dequeue
# peek
# isEmpty
# size




class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
      

        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    



queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("queue.peek(): ", queue.peek())
print("queue.size(): ", queue.size())


print("queue.isEmpty(): ", queue.isEmpty())
print("queue.dequeue(): ", queue.dequeue())

