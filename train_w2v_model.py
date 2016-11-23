# -*- coding: utf-8 -*


from gensim.models import word2vec

from util.functions import trace, check_directory
from util.cinstants import *


if __name__ == '__main__':

    trace("check directory")
    dir_path = [W2V_MECAB_MODEL, W2V_JUMAN_MODEL]
    check_directory(dir_path)

    trace("load mecab wakati file")
    data = word2vec.Text8Corpus(WAKATI_MECAB)
    trace("train mecab word2vec")
    model = word2vec.Word2Vec(data, size=UNIT)
    trace("save mecab word2vec model")
    model.save(W2V_MECAB_MODEL)

    trace("load juman wakati file")
    data = word2vec.Text8Corpus(WAKATI_JUMAN)
    trace("train juman word2vec")
    model = word2vec.Word2Vec(data, size=UNIT)
    trace("save juman word2vec model")
    model.save(W2V_JUMAN_MODEL)

    trace("finish!")
