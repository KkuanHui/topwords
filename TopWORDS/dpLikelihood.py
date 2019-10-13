from . import tlimit as tl

"""
Ultilize dynamic programming to compute likelihood [P(sentence| D)].
"""
def forward_dplikelihood(sentence, dict_0, taul):
    likelihood = [0] * len(sentence)
    likelihood[0] = 1.0
    for m in range(len(sentence)-1):
        tlimit = tl.frowardtlimit(m, taul)
        for j in tlimit:
            word = sentence[m-j: m]
            if(word in dict_0._dict.keys()):
                likelihood[m] += likelihood[m-j] * dict_0._dict[word]
    return likelihood


def backward_dplikelihood(sentence, dict_0, taul):
    likelihood = [0] * len(sentence)
    likelihood[-1] = 1.0
    for m in reversed(range(len(sentence))):
        tlimit = tl.backwardtlimit(sentence, m, taul)
        for j in tlimit:
            word = sentence[m:m+j]
            if(word in dict_0._dict.keys()):
                likelihood[m] += dict_0._dict[word] * likelihood[m+j] 
    return likelihood
