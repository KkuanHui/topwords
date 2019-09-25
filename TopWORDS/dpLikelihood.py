

"""
Ultilize dynamic programming to compute likelihood [P(sentence| D)].
"""
def forward_dplikelihood(sentence, dict_0, taul):
    likelihood = [0] * len(sentence)
    likelihood[0] = 1.0
    for m in range(len(sentence)-1):
        if m+taul >= len(sentence):
            tlimit = len(sentence)-m
        else:
            tlimit = taul
        for j in tlimit:
            word = sentence[m: m+j]
            if(word in dict_0.keys()):
                likelihood[m+j] = likelihood[m] * dict_0[word]
                

def backward_dplikelihood(sentence, dict_0, taul):
    likelihood = [0] * len(sentence)
    likelihood[-1] = 1.0
    for m in reversed(range(len(sentence-1))):
        if m-taul <= 0:
            tlimit = m
        else:
            tlimit = taul
        for j in tlimit:
            word = sentence[m-j, m]
            if(word in dict_0.keys()):
                likelihood[m-j] = likelihood[m] * dict_0[word]
