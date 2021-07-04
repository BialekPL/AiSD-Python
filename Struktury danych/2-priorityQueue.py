# Zadnie 2 - kolejka priorytetowa, użycie kopca
# Queue can hold up to 7 elements
class priotiyQueue():
    def __init__(self):
        self.pq = 8 * [None]
        self.len = 0

    def enqueue(self, element):
        if self.len < 7:
            self.len += 1
            self.pq[self.len] = element
            self.__moveUp()
        else: print("Queue is full! Dequeue some element before adding another.")
        

    def dequeue(self):
        if self.len > 0:
            element = self.pq[1]
            
            if self.len > 1:
                # get last element on top and get everything in order by movingDown 
                self.pq[1] = self.pq[self.len]
                self.__moveDown()
            self.len -= 1
            return element
             
        else: return "Queue is empty! Enqueue some element before dequeuing."

    def __moveUp(self):
        n = self.len
        while(n!=1):
            upper = int(n/2)
            if self.pq[n] > self.pq[upper]:
                self.pq[n], self.pq[upper] = self.pq[upper], self.pq[n]
                n = upper
            else: break

    def __moveDown(self):
        n = 1 # Top node
        while (True):
            child = 2 * n
            # if left child doesnt exist then we done
            if child > self.len:
                break 
            
            #if right child exist we determine which is bigger
            if (child+1 <= self.len): 
                if self.pq[child] < self.pq[child+1]: child +=1 

            #if theres no bigger nodes among children then we done
            if self.pq[n] > self.pq[child]:
                break 
            else:
                # we go one node deeper
                self.pq[n], self.pq[child] = self.pq[child], self.pq[n]
                n = child

pq1 = priotiyQueue()
print(pq1.dequeue())
pq1.enqueue(1)
pq1.enqueue(3)
pq1.enqueue(3)
pq1.enqueue(4)
pq1.enqueue(2)
pq1.enqueue(6)
pq1.enqueue(7)
pq1.enqueue(8)
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())



