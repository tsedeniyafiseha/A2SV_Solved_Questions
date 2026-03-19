from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = deque()
        
    def insertFront(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        self.queue.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        self.queue.append(value)
        return True
    
    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False
        
    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        return False
        
    def getFront(self) -> int:
        return self.queue[0] if self.queue else -1

    def getRear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        return len(self.queue) == self.k