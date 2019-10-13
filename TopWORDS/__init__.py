
from . import dictionary
from . import dplikelihood
from . import excorpus_sos
from . import preprocessing
from . import segment
from . import updatetheta

"""
Because of TopWORDS involving EM algorithm that require tune paracmeter, it can only be implemented in class.
"""
class TopWORDS:
    def __init__(self, corpus, taul = 10, tauf = 5, useprob = 1e-5, itertime = 10, convergethld = 1E-3, segmentthld = 0.1):
        self.corpus = corpus
        self.taul = taul
        self.tauf = tauf
        self.useprob = useprob
        self.itertime = itertime
        self.convergethld = convergethld
        self.segmentthld = segmentthld

        self.dict_0 = dictionary.dictionary()
        self.dict_1 = dictionary.dictionary()
        self.result_text = []

    def run(self):
        # 1. preprocess corpus
        self.text = preprocessing.preprocessing(self.corpus)
        # 2. build initial dictionary
        # self.dict_0 = dictionary.dictionary()
        self.dict_0.initial_dict(self.text, self.taul, self.tauf, self.useprob) 
        # 3. start EM
        converge = False
        lastlikelihood = -1.0
        iterconut = 0
        # the loop
        print("Max itertime:", self.itertime)
        while(not converge or self.itertime != iterconut):
            print("Itertime:",iterconut+1)
            # 3.1 make a updated and pruned new dictionary dict_1
            updatetheta.updatetheta(self.text, self.taul, self.dict_0, self.dict_1, self.useprob)
            # 3.2 compare lastlikelihood with likelihood
            newlikelihood = 0
            for sentence in self.text:
                likelihd = dplikelihood.backward_dplikelihood(sentence, self.dict_0, self.taul)
                newlikelihood += likelihd[0]
            if lastlikelihood/newlikelihood < self.convergethld and iterconut != 0:
                converge = True
            lastlikelihood = newlikelihood
            iterconut += 1
            self.dict_0 = self.dict_1
            self.dict_1 = dictionary.dictionary()
        # 4. segment corpus
        for sentence in self.text:
            back_dpl = dplikelihood.backward_dplikelihood(sentence, self.dict_0, self.taul)
            for_dpl  =  dplikelihood.forward_dplikelihood(sentence, self.dict_0, self.taul)
            result = segment.segment(sentence, self.segmentthld, for_dpl, back_dpl)
            self.result_text += [result]
            
