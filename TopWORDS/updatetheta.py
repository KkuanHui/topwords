

from . import tlimit as tl
from . import dplikelihood as dl
from . import dpcache as dc
from . import dictionary as dt

"""
Update theta's estimate.
Use backward strategy.
Must notice how estimates change in the estimation process. 
return dict_1
"""

def updatetheta(text, taul, dict_0):
    dict_1 = dt.dictionary()
    nj_T = dc.dpcache()
    for sentence in text:
        backward_likelihood = dl.backward_dplikelihood(sentence, dict_0, taul)
        for m in range(reversed(len(sentence))):
            tlimit = tl.backwardtlimit(sentence, m, taul)
            cuttings = []
            # cuttings = [(word, j, rho)]
            for j in tlimit:
                word = sentence[m: m+j]
                if word in dict_0.keys(): rho = (dict_0[word] * backward_likelihood[m+j])/ backward_likelihood[m]
                else: rho = 0
                cuttings += [(word, j, rho)]
            # compute dp nj_T
            # here
            nj_T.push(cuttings)
    for word_i, nj in nj_T.top().items():
        if word_i in dict_1._dict.keys(): dict_1._dict[word_i] += nj
        else: dict_1._dict[word_i] = nj
    dict_1.normalize_dictionary()
    dict_1.prune_dictionary_prob()
    dict_1.normalize_dictionary()
    # return a updated and pruned dictionary dict_1
    return dict_1
