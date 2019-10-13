

"""
check tlimit
"""

def frowardtlimit(m, taul):
    if m - taul < 0:
        tlimit = list(range(m)[1:])
    else:
        tlimit = list(range(taul)[1:])
    return tlimit

def backwardtlimit(sentence, m, taul):
    if m == len(sentence):
        tlimit = [1]
    elif m + taul > len(sentence):
        a = len(sentence) - m
        tlimit = list(range(a)[1:])
    else:
        tlimit = list(range(taul)[1:])
    return tlimit
