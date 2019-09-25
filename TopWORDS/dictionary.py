

"""
Build initial dictionary
"""
from collections import Counter

def cut_words(text, taul):
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
    return word_ls


"""
Dictionary contains words and its relevent theta.
"""
def overcomplete_dictionary(word_ls, tauf, useprob):
    # prune by appearence times
    dict_0 = [k: v for k, v in Counter(word_ls).items if len(k) == 1 or v >= tauf]
    sum_theta = sum(dict_0.values())
    dict_0 = [k: (v/sum_theta) for k, v in dict_0.items]
    # prune by reletive probability
    dict_0 = [k: v for k, v in dict_0.items if len(k)==1 or v >= useprob]
    sum_theta = sum(dict_0.values())
    dict_0 = [k: (v/sum_theta) for k, v in dict_0.items]
