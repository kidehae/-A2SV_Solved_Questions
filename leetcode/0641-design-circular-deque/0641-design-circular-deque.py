class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.cir_queue = deque()
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.length < self.k:
            self.cir_queue.appendleft(value)
            self.length += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.length < self.k:
            self.cir_queue.append(value)
            self.length += 1
            return True
        return False


    def deleteFront(self) -> bool:
        if self.cir_queue:
            self.cir_queue.popleft()
            self.length -= 1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.cir_queue:
            self.cir_queue.pop()
            self.length -= 1
            return True
        return False
        

    def getFront(self) -> int:
        if self.cir_queue:
            return self.cir_queue[0]
        return(-1)

    def getRear(self) -> int:
        if self.cir_queue:
            return self.cir_queue[-1]
        return(-1)
        

    def isEmpty(self) -> bool:
        return not self.cir_queue
        

    def isFull(self) -> bool:
        return self.length == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()