
"""
Build initial dictionary
"""
from collections import Counter


class dictionary:
    def __init__(self):
        self._dict = {}

    def initial_dict(self, text, taul, tauf, useprob):
        word_ls = []
        for sentence in text:
            for m in range(len(sentence)-1):
                if m+taul >= len(sentence):
                    tlimit = len(sentence)-m
                else:
                    tlimit = taul
                for j in range(len(taul)):
                    word = sentence[m:m+j]
                    word_ls.append(word)
        # prune by appearence times
        self._dict = {k: v for k, v in Counter(word_ls).items if len(k) == 1 or v >= tauf}
        sum_theta = sum(self._dict.values())
        self._dict = {k: (v/sum_theta) for k, v in self._dict.items()}
        # prune by reletive probability
        self._dict = prune_dictionary_prob(self._dict)

    def prune_dictionary_prob(self, useprob):
        self._dict = {k: v for k, v in self._dict.items() if len(k)==1 or v >= useprob}
        sum_theta = sum(self._dict.values())
        self._dict = {k: (v/sum_theta) for k, v in self._dict.items()}

    def normalize_dictionary(self):
        total = sum(self._dict.values())
        self._dict = {k: v/total for k, v in self._dict}
