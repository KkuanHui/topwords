

"""
Preprocess original corpus.
Segment target chinese corpus into sentences by punchuation or non chinese words.
"""


def preprocessing(corpus):
    reChinese = re.compile('[\u4e00-\u9fa5]+') 
    return reChinese.findall(corpus)
