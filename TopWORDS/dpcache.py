

from . import limitstack as limstk

"""
work with limitstack
"""

class dpcache:
    def __init__(self, taul):
        self.cache = {}
        self.taul = taul
    def push(self, cuttings):
        # cuttings = [(word, j, rho)]
        for item in cuttings:
            if item[0] not in self.cache.keys():
                self.cache[item[0]] = limstk.limitstack(self.taul, 0)
        for word_i in self.cache.keys():
            value = 0
            for item in cuttings:
                if item[0] == word_i: 
                    value += item[2] * (1 + self.cache[word_i].get(item[1]-1))
                else:
                    value += item[2] * (0 + self.cache[word_i].get(item[1]-1))
            self.cache[word_i].push(value)

    def top(self):
        return {k : v.get(0) for k, v in self.cache.items()}
