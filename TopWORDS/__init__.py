
from . import dictionary
from . import dpcache
from . import dplikelihood
from . import excorpus_sos
from . import limitstack
from . import preprocessing
from . import segment
from . import tlimit
from . import updatetheta

"""
Because of TopWORDS involving EM algorithm that require tune paracmeter, it can only be implemented in class.
"""
class TopWORDS:
    def __init__(self, corpus, taul = 10, tauf = 5, useprob = 1E-8, itertime = 10, convergethld = 1E-3, segmentthld = 0.0):
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
        while(not converge or self.itertime != iterconut):
            # 3.1 make a updated and pruned new dictionary dict_1
            dict_1 = updatetheta.updatetheta(self.text, self.taul, self.dict_0)
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
"excorpus_sos.sos"

if __name__ == "__main__":
    a = excorpus_sos.sos
    TW = TopWORDS(a)
    TW.run()





