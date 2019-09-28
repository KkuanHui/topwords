from . import dictionary
from . import preprocessing
from . import dplikelihood
from . import updatetheta


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
        text = preprocessing.preprocessing(self.corpus)
        # 2. build initial dictionary
        word_ls = dictionary.cut_words(text, self.taul)
        dict_0 = dictionary.overcomplete_dictionary(word_ls, self.tauf, self.useprob)
        # 3. start EM
        converge = False
        lastlikelihood = -1.0
        iterconut = 0
        while(!converge or itertime == iterconut):
            converge = False
            # 3.1 update theta
            dict_1 = updatetheta(text, self.taul, dict_0)
            # 3.2 prune dict_1
            dict_1 = dictionary.prune_dictionary_prob(dict_1)
            # 3.3 compare lastlikelihood with likelihood
            
            newlikelihood = 0
            for sentence in text:
                newlikelihood += dplikelihood.backward_dplikelihood(dict_0)
            if lastlikelihood/newlikelihood < convergethld and iterconut != 0:
                converge = True
            lastlikelihood = newlikelihood
            iterconut += 1
            dict_0 = dict_1
        # 4. segment corpus
        for sentence in text:
            back_dpl = dplikelihood.backward_dplikelihood(sentence, dict_1, self.taul)
            for_dpl =  dplikelihood.forward_dplikelihood(sentence, dict_1, self.taul)
            for m in range(len(sentence)):
                if back_dpl[m] * for_dpl[m] > self.segmentthld:
                    #segment sentence at place m





if __name__ == "__main__":
    corpus = """
    超人出生於克利普頓星，親生父母為他命名凱艾爾；在克利普頓星爆炸前，還是嬰兒的凱·艾爾被身為科學家的父親喬艾爾用太空船送往地球。超人是一個超級英雄，超級英雄的工作是救人、救地球、救世界。超人的名字為艾爾，全名為凱艾爾，他的地球名字為克拉克，超人來自於克利普頓星，他的父母親都是克利普頓人的高層官員，在政府的高層進行行政工作，從而了解到克利普頓星的滅亡在即，超人的父母親將幼兒時期的超人放進太空船中送往地球來。
    """
