

from . import limitstack as limstk

"""
work with limitstack
"""

class dpcache:
    def __init__(self):
        self.cache = {}
    def push(self, cuttings):
        # cuttings = [(word, j, rho)]
        for item in cuttings:
            if item[0] not in self.cache.keys():
                self.cache[item[0]] = limstk.limitstack(item[1], 0)
        for item in cuttings:
            for word_i in self.cache.keys():
                if item[0] == word_i:
                    value = item[2] * (1 + self.cache[item[0]].get(j-1))
                    self.cache[item[0]].push(value) 
                else:
                    value = item[2] * (self.cache[item[0]].get(j-1))
                    self.cache[item[0]].push(value)
    def top(self):
        return {k : v.get(0) for k, v in self.cache.items()}
