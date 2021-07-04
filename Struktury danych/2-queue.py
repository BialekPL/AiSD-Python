# Zadnie 2 - kolejka
class Queue():
    def __init__(self):
        # Queue will be able to hold up to 4 elements, so we have to have 5 elements long list
        self.queue = 5 * [None]
        self.head = 0
        self.tail = 0
    
    def enqueue(self, element):
        if self.head != (self.tail + 1) % 5: 
            self.queue[self.tail] = element
            self.tail = (self.tail + 1) % 5
        else: print("Queue is full! Can't add this element.")

    def dequeue(self):
        if self.head != self.tail:
            element = self.queue[self.head]
            self.head = (self.head + 1) % 5 
            return element
        else: return "Queue is empty, enqueue some element before dequeuing"


q1 = Queue()
print(q1.dequeue())
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1.dequeue())
print(q1.dequeue())
q1.enqueue(6)
print(q1.dequeue())
q1.enqueue(7)
q1.enqueue(8)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())




