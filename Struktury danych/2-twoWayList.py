
# Zadnie 2 - kolejka dwustronna
class twoWayList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        pass

    def add(self, element, index):
        if index > self.len or index < 0:
            print("Can't add that element on that position.")
            return False;
        
        current = self.head
        #if there are no items in the list yet
        if current is None:
            self.head = element
            self.tail = element
        
        else:
            for _ in range(0, index):
                current = current.next
            #adding to the end
            if current is None:
                element.prev = self.tail
                self.tail.next = element
                self.tail = element
            #if current isn't first on list
            elif current.prev is not None:
                current.prev.next = element
                element.prev = current.prev
                element.next = current
                current.prev = element
            #adding to the beginning
            else:
                element.next = self.head
                self.head = element
                current.prev = element
        self.len += 1
        return True
            

    def remove(self, index):
        if index > self.len-1 or index < 0:
            print("Can't remove element with given index")
            return 1 

        current = self.head
        for _ in range(index):
            current = current.next
        
        if current.next is not None:
            if current.prev is not None:
                current.prev.next = current.next
            else:
                self.head = current.next    
            current.next.prev = current.prev
        else:
            if current.prev is not None:
                current.prev.next = current.next 
            else:
                self.head = None
            self.tail = current.prev
        self.len -= 1

    def printList(self, reversed=False):
        if not reversed:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next
        else:
            current = self.tail
            while current is not None:
                print(current.value)
                current = current.prev

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                print("There is an element in the list with given value.")
                return 0
            else:
                current = current.next
        print("There is no element in the list with given value.")

class listElement():
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value
    #def __del__(self):
        #print("destroyed")
    def __str__(self):
        return f"Node with value = {self.value}"
    def __repr__(self):
        return f"Node with value = {self.value}"



twl = twoWayList()
e1 = listElement(1)
e2 = listElement(2)
e3 = listElement(3)
e4 = listElement(7)
e5 = listElement(8)
e6 = listElement(9)

twl.add(e1,2)
twl.add(e1,0)
twl.add(e2,1)
twl.add(e3,2)
twl.add(e4,3)
twl.search(1)
twl.search(0)
print("list: ")
twl.printList()
print("reversed list: ")
twl.printList(reversed=True)
twl.remove(2)
print("list: ")
twl.printList()





