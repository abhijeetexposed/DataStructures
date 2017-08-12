class Deque:
    Capacity = 10 

    def __init__(self):
       
        self.data = [None]*Deque.Capacity
        self.size = 0
        self.front = 0 # index for handling frontier of the deque
        self.back = 0 # index of handling back of the deque 
    
    def isEmpty(self):
        return self.size == 0
    
    def frontElement(self):
        return self.data[self.front]
    
    def backElement(self):
        return self.data[self.size-1]
    
    def enqueueback(self, element):
        if self.size >= len(self.data):
            self._resizeBack()
        
        self.data[self.back] = element
        self.back += 1
        self.size += 1

    def dequeueFront(self):
        if self.isEmpty():
            print("Deque is empty")
        else:
            temp = self.data[self.front]
            self.data[self.front] = None
            self.front += 1
            self.size -= 1
    
    def enqueuefront(self, element):
        if not self.data[self.front-1] == None:
            print("Can't insert element in front")
        else:
            if (self.front - 1) > 0:
                self.front -= 1
                self.data[self.front] = element
            else:
                self.data[self.front] = element 
                
            self.size += 1   

    def dequeueBack(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            temp = self.data[self.back]
            self.data[self.back] = None
            self.back -= 1
            self.size -= 1

    def _resizeBack(self):
        print(self.size)
        
        temp = [None]*(2*len(self.data))
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = [None]*2*len(self.data)
        self.data = temp
