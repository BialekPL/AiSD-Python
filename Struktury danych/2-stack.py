# Zadnie 2 - stos
# Requires python>=3.6 (I'm using fstrings, i.e. line 27)
class Stack():

    def __init__(self, stack_len):
        self.max_len = stack_len
        self.top = -1
        self.stack = stack_len*[None] 
   
    def push(self, element):
        if self.top < 3:
            self.top += 1
            self.stack[self.top] = element
        else: print("Stack is full! Pop some element before adding another.")

    def pop(self):
        if self.top > -1:
            element = self.stack[self.top]
            self.top -= 1
            return element
        else: return "Stack is empty! Add some element before popping."

SIZE = 4

stack1 = Stack(SIZE)
print(f"Stack is able to hold up to {SIZE} elements")
print(stack1.pop())
stack1.push(1)
stack1.push(2)
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
stack1.push(6)
stack1.push(7)
stack1.push(8)
stack1.push(9)
stack1.push(10)
stack1.push(11)
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
