class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {v: i for i, v in enumerate(list1)}
        min_sum = float('inf')
        result = []
        
        for j, name in enumerate(list2):
            if name in index_map:
                total = j + index_map[name]
                
                if total < min_sum:
                    min_sum = total
                    result = [name]
                elif total == min_sum:
                    result.append(name)
                    
        return result
