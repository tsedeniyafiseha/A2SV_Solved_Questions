class Solution(object):
    def countCharacters(self, words, chars):
        from collections import Counter
        
        char_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            valid = True
            
            for c in word_count:
                if word_count[c] <= char_count.get(c, 0):
                    continue   
                else:
                    valid = False
                    break     
            
            if valid:
                total_length += len(word)
                
        return total_length
