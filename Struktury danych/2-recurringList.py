# Zadnie 2 - kolejka cykliczna
class recurringList():
    def __init__(self):
        self.head = None
        self.len = 0
        
    
    def printElements(self):
        current = self.head
        if current is None: print("List is empty.")
        else:
            print(current.value)
            current = current.next
            if current is not None:
                while current is not self.head:
                    print(current.value)
                    current = current.next

    def search(self, value):
        if self.len == 0: return "That value is not present on the list"
        
        if self.head.value == value:
            return "That value is present on the list"
        current = self.head.next
        if current is not None:
            while current is not self.head:
                    if current.value == value:
                        return "That value is present on the list"
                    current = current.next
        return "That value is not present on the list"

    def add(self, element, index):
        if index > self.len or index < 0:
            return "Can't add that element on that position."
            
        else:
            # Adding to the beginning  
            if index == 0:
                element.next = self.head
                if element.next is None:
                    element.next = element
                self.head = element
            else:
                current = self.head
                for _ in range(0,index):
                    current = current.next
                if current is not None:
                    element.next = current
                else:
                    # making recurring list there, last element.next points to fisrt element 
                    element.next = self.head
                current = self.head
                for _ in range(0, index-1):
                    current = current.next
                current.next = element
            self.len += 1
            return "Element added."

    def remove(self, index):
        if index > self.len-1 or index < 0:
            print("Can't remove element with given index")
            return 1    
        #removing from the beginnning
        if index == 0:
            #if it was the only item:
            if self.len == 1:
                self.head = None 
            else:
                self.head = self.head.next
                lastItem = self.head
                for _ in range(self.len-1):
                    lastItem = lastItem.next 
                lastItem.next = self.head
        
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
            
        self.len -= 1
    

class listElement():
    def __init__(self, value):
        self.next = None
        self.value = value


rl = recurringList()
rl.search(2)
e1 = listElement(3)
e2 = listElement(4)
e3 = listElement(5)
e4 = listElement(6)
print(rl.add(e1,0))
print(rl.add(e2,1))
print(rl.add(e3,2))
print(rl.add(e4,3))
print("list: ")

rl.printElements()
print(rl.search(3))
print(rl.search(1))
rl.remove(3)
print("list: ")
rl.printElements()
rl.remove(2)
print("list: ")
rl.printElements()
rl.remove(1)
print("list: ")
rl.printElements()
rl.remove(0)
print("list: ")
rl.printElements()
print(rl.add(e1,0))
print(rl.add(e4,1))
rl.printElements()


