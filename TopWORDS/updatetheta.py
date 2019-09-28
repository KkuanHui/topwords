

from . import tlimit as tl
from . import dplikelihood as dl

"""
Update theta's estimate.
Use backward strategy.
"""



def updatetheta(text, taul, dict_0):
    dict_1 = {k:0 for k in dict_0.keys()}
    for sentence in text:
        likelihood = dl.backward_dplikelihood(sentence, dict_0, taul)
        dict_cache = {k:0 for k in dict_0.keys()}
        for m in range(reversed(len(sentence))):
            tlimit = tl.backwardtlimit(sentence, m, taul)
            for j in tlimit:
                word = sentence[m: m+j]
                if word in dict_0.keys():
                    # cache
                    rho = (dict_0[word] * likelihood[m+j])/ likelihood[m]
                    dict_cache[word] = rho(1 + dict_cache[word])
        for word in dict_0.keys():
            dict_1[word] += dict_cache[word]
    total = sum(dict_1.values())
    dict_1 = [k: v/total for k, v in dict_cache.items()]
    return dict_1

