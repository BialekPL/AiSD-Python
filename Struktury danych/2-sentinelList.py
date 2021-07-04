# Zadnie 2 - kolejka jednostronna z wartownikiem
class sentinelList():
    def __init__(self):
        self.sentinel = listElement(None)
        self.head = self.sentinel
        self.len = 0

    def add(self, element, index):
        if index > self.len or index < 0:
            print("Can't add that element on that position.")
            return 1
        
        # Adding to beginning 
        if index==0:
            element.next = self.sentinel.next
            self.sentinel.next = element
        # adding to the end of the list 
        if index==self.len:
            element.next = self.sentinel
            current = self.sentinel
            for _ in range(index):
                current = current.next
            current.next = element
        # adding somewhere in the middle
        elif index!=0:
            current = self.sentinel
            for _ in range(index+1):
                current = current.next
            element.next = current
            current = self.head
            for _ in range(index):
                current = current.next
            current.next = element
        self.len+=1

    
    def remove(self, index):
        if index > self.len or index < 0:
            print("Can't remove element with given index")
            return 1    

        prev = self.sentinel
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        if prev.next is None:
            prev.next = self.sentinel

        self.len -= 1


    def search(self, value):
        self.sentinel.value = value
        current = self.sentinel.next
        if current is not None:
            while current.value != value:
                current = current.next
            if current is not self.sentinel:
                print("There is an element with given value in the list")
                self.sentinel.value = None
                return 0
            
        print("There is no such element in the list")
        self.sentinel.value = None

    def printElements(self):
        current = self.sentinel.next
        if current is not None:
            while current is not self.sentinel:
                print(current.value)
                current = current.next


class listElement():
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f"Node with value {self.value}"
    def __repr__(self):
        return f"Node with value {self.value}"

sl = sentinelList()
e1 = listElement(1)
e2 = listElement(2)
e3 = listElement(3)
e4 = listElement(4)
e5 = listElement(5)
e6 = listElement(6)

sl.add(e1,0)
sl.add(e2,1)
sl.add(e3,2)
sl.add(e4,3)
sl.add(e5,4)

sl.search(1)
sl.search(6)

sl.printElements()
sl.remove(0)
sl.add(e6,0)
sl.printElements()

