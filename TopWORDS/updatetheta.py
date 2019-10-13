

from . import tlimit as tl
from . import dplikelihood as dl
from . import dpcache as dc

"""
Update theta's estimate.
Use backward strategy.
Must notice how estimates change in the estimation process. 
return dict_1
"""

def updatetheta(text, taul, dict_0, dict_1, useprob):
    nj_T = dc.dpcache(taul)
    for sentence in text:
        backward_likelihood = dl.backward_dplikelihood(sentence, dict_0, taul)
        #print(backward_likelihood)
        print("###",sentence)
        for m in reversed(range(len(sentence))):
            print("m=",m)
            tlimit = tl.backwardtlimit(sentence, m, taul)
            print(tlimit)
            cuttings = []
            # cuttings = [(word, j, rho)]
            for j in tlimit:
                word = sentence[m: m+j]
                print(word)
                if word in dict_0._dict.keys(): 
                    rho = (dict_0._dict[word] * backward_likelihood[m+j])/ backward_likelihood[m]
                cuttings += [(word, j, rho)]
            # compute dp nj_T
            nj_T.push(cuttings)
    for word_i, nj in nj_T.top().items():
        if word_i in dict_1._dict.keys(): dict_1._dict[word_i] += nj
        else: dict_1._dict[word_i] = nj
    dict_1.normalize_dictionary()
    dict_1.prune_dictionary_prob(useprob)
    dict_1.smooth_dictionary(useprob)
    dict_1.normalize_dictionary()
