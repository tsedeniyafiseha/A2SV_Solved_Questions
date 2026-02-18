import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val):
        if val in self.index_map:
            return False
        
        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.index_map:
            return False
        
        # Get index of element to remove
        remove_index = self.index_map[val]
        
        # Get last element
        last_element = self.nums[-1]
        
        # Move last element into removed spot
        self.nums[remove_index] = last_element
        self.index_map[last_element] = remove_index
        
        # Remove last element
        self.nums.pop()
        del self.index_map[val]
        
        return True

    def getRandom(self):
        return random.choice(self.nums)
