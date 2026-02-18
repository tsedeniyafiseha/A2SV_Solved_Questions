class FrequencyTracker(object):

    def __init__(self):
        self.count_map = {}
        self.freq_map = {}

    def add(self, number):
        old_freq = self.count_map.get(number, 0)
        new_freq = old_freq + 1
        
        self.count_map[number] = new_freq
        
        if old_freq > 0:
            self.freq_map[old_freq] -= 1
        
        self.freq_map[new_freq] = self.freq_map.get(new_freq, 0) + 1

    def deleteOne(self, number):
        if number not in self.count_map or self.count_map[number] == 0:
            return
        
        old_freq = self.count_map[number]
        new_freq = old_freq - 1
        
        self.count_map[number] = new_freq
        
        self.freq_map[old_freq] -= 1
        
        if new_freq > 0:
            self.freq_map[new_freq] = self.freq_map.get(new_freq, 0) + 1

    def hasFrequency(self, frequency):
        return self.freq_map.get(frequency, 0) > 0
