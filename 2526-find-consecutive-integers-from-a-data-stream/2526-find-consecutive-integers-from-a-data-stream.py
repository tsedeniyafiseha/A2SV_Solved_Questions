from collections import deque

class DataStream(object):

    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.q = deque()
        self.count = 0

    def consec(self, num):

        self.q.append(num)

        if num == self.value:
            self.count += 1

        if len(self.q) > self.k:
            removed = self.q.popleft()
            if removed == self.value:
                self.count -= 1

        return self.count == self.k