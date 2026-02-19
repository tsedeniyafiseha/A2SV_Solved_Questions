from collections import Counter

class Solution(object):
    def findCommonResponse(self, responses):
        count = Counter()

        for person in responses:
            unique = set(person)   
            for word in unique:
                count[word] += 1

        max_freq = max(count.values())

        result = ""
        for word in count:
            if count[word] == max_freq:
                if result == "" or word < result:
                    result = word

        return result
