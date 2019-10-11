

"""
Segmentor is used to segment a sentence.

0b1i2g
"""


def segment(sentence, segmentthld, forward_dplikelihood, backward_dplikelihood):
    boundary = [(j, 0) for j in range(len(sentence))]
    for m in range(len(sentence-2)):
        value = (forward_dplikelihood[m] * backward_dplikelihood[m])/backward_dplikelihood[0]
        if value > segmentthld: boundary[m] = 1
        else: boundary[m] = 0
    idx = 0
    for i in boundary:
        if i[1] == 1:
            sentence=sentence[:i[0]+idx]+"|"+sentence[i[0]+idx:]
            idx+=1
    return sentence
