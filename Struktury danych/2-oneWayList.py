# Zadnie 2 - kolejka jednostronna
class oneWayList():
    def __init__(self):
        self.head = None
        self.len = 0
    
    def printElements(self):
        current = self.head
        if current is None: print("List is empty.")
        else:
            while(current is not None):
                print (current.value)
                current = current.next

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return "That value is present in the list." 
            else:
                current = current.next
        return "That value is not present in the list"

    def add(self, element, index):
        if index > self.len or index < 0:
            return "Can't add that element on that position."
            
        if index == 0:
            element.next = self.head
            self.head = element
        else:
            current = self.head
            for _ in range(0,index):
                current = current.next
            element.next = current
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
        if index == 0:
            self.head = self.head.next
        else:
            previous = self.head
            for _ in range(index-1):
                previous = previous.next
            previous.next = previous.next.next
        self.len -= 1

class listElement():
    def __init__(self, value):
        self.next = None
        self.value = value
    
owl = oneWayList()
e1 = listElement(1)
e2 = listElement(2)
e3 = listElement(3)
e4 = listElement(7)

print(owl.add(e1,0))
print(owl.add(e2,1))
print(owl.add(e3,2))
print(owl.add(e4,3))
print(owl.add(e4,5))
print(owl.add(e4,-2))

owl.printElements()

print(owl.search(5))
print(owl.search(1))
owl.remove(3)
owl.printElements()

