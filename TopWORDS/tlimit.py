

"""
check tlimit
"""

def frowardtlimit(m, taul):
    if m - taul < 0:
        tlimit = m
    else:
        tlimit = taul
    return tlimit

def backwardtlimit(sentence, m, taul):
    if m + taul > len(sentence):
        tlimit = len(sentence) - m
    else:
        tlimit = taul
    return tlimit
