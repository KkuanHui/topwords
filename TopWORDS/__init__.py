from . import dictionary
from . import preprocessing
from . import dplikelihood
from . import updatetheta
from . import segment

from . import *


"""
Because of TopWORDS involving EM algorithm that require tune paracmeter, it can only be implemented in class.
"""
class TopWORDS:
    def __init__(self, corpus, taul, tauf, useprob, itertime, convergethld, segmentthld):
        self.corpus = corpus
        self.taul = taul
        self.tauf = tauf
        self.useprob = useprob
        self.itertime = itertime
        self.convergethld = convergethld
        self.segmentthld = segmentthld

    def run(self):
        # 1. preprocess corpus
        self.text = preprocessing.preprocessing(self.corpus)
        # 2. build initial dictionary
        self.dict_0 = dictionary.dictionary()
        self.dict_0.initial_dict(self.text, self.taul, self.tauf, self.useprob) 
        # 3. start EM
        converge = False
        lastlikelihood = -1.0
        iterconut = 0
        # the loop
        while(!converge or self.itertime == iterconut):
            # 3.1 make a updated and pruned new dictionary dict_1
            dict_1 = updatetheta(self.text, self.taul, dict_0)
            # 3.2 compare lastlikelihood with likelihood
            newlikelihood = 0
            for sentence in text:
                newlikelihood += dplikelihood.backward_dplikelihood(dict_0._dict)
            if lastlikelihood/newlikelihood < convergethld and iterconut != 0:
                converge = True
            lastlikelihood = newlikelihood
            iterconut += 1
            self.dict_0 = dict_1
        # result dictionary is still dict_0
        # 4. segment corpus
        self.result_text = []
        for sentence in self.text:
            back_dpl = dplikelihood.backward_dplikelihood(sentence, self.dict_0, self.taul)
            for_dpl  =  dplikelihood.forward_dplikelihood(sentence, self.dict_0, self.taul)
            result = segment.segment(sentence, self.segmentthld, for_dpl, back_dpl)
            self.result_text += [result]


if __name__ == "__main__":
    corpus = """
    超人出生於克利普頓星，親生父母為他命名凱艾爾；在克利普頓星爆炸前，還是嬰兒的凱·艾爾被身為科學家的父親喬艾爾用太空船送往地球。超人是一個超級英雄，超級英雄的工作是救人、救地球、救世界。超人的名字為艾爾，全名為凱艾爾，他的地球名字為克拉克，超人來自於克利普頓星，他的父母親都是克利普頓人的高層官員，在政府的高層進行行政工作，從而了解到克利普頓星的滅亡在即，超人的父母親將幼兒時期的超人放進太空船中送往地球來。
    """
