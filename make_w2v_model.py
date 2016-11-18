# -*- coding: utf-8 -*

from gensim.models import word2vec

TRAIN_PATH      = "./data/wakati/train_w2v.txt"
WAKATI_W2V_PATH = "./data/wakati/wakati_w2v.txt"
MODEL_PATH_CNN  = "./data/w2v_model/model_cnn"
MODEL_PATH_ALL  = "./data/w2v_model/model_all"
UNIT            = 300

if __name__ == '__main__':
    # CNN
    data = word2vec.Text8Corpus(TRAIN_PATH)
    model = word2vec.Word2Vec(data, size=UNIT)
    model.save(MODEL_PATH_CNN)
    # ALL
    data = word2vec.Text8Corpus(WAKATI_W2V_PATH)
    model = word2vec.Word2Vec(data, size=UNIT)
    model.save(MODEL_PATH_ALL)
