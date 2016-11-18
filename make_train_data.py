# -*- coding: utf-8 -*-


import sys
import pickle

import numpy
from gensim.models import word2vec
from chainer import cuda


WAKATI_PATH     = "./data/wakati/mini_data.txt"
#WAKATI_PATH     = "./data/wakati/wakati.txt"
MODEL_PATH      = "./data/w2v_model/model_all"
TRAIN_DATA_PATH = "./data/train_dataset/mecab_w2v.pkl"
META_SPLIT      = "<hogefugapiyo>"
UNIT            = 300
GPU             = -1
SEED            = 123

xp = cuda.cupy if GPU >= 0 else numpy
xp.random.seed(SEED)

class MakeTrainData():

    def __init__(self, model_path, wakati_path):
        self.wakati_path = wakati_path
        self.model_path  = model_path

    def init_set(self):
        self.__model      = word2vec.Word2Vec.load(self.model_path)
        self.__train_data = self.__read_doc(self.wakati_path)
        self.__train_data = self.__add_vec2train_data(self.__train_data)
        self.label_dict   = self.__get_label_dict(self.__train_data)

    def get_train_data(self):
        label = [self.label_dict[i["label"]] for i in self.__train_data]
        vec = xp.array([i["vec"] for i in self.__train_data])
        f_size = vec.shape[1]*vec.shape[2]
        vec = vec.reshape((-1, f_size))
        return label, vec

    def __read_doc(self, path):
        train_data  = []
        with open(path, mode='r') as f:
            for line in f:
                no, lab, txt = str(line).split(META_SPLIT)
                one = {"id":no, "label":lab, "text":txt.split()}
                train_data.append(one)
        max_h = max(len(i["text"]) for i in train_data)
        train_data = self.__padding(train_data, max_h)
        return train_data

    def __padding(self, train_data, max_h):
        for i, data in enumerate(train_data):
            pad_txt = ['<pad>' for i in range(max_h - len(data["text"]))]
            train_data[i]["text"] += pad_txt
        return train_data

    def __add_vec2train_data(self, train_data):
        for data in train_data:
            data["vec"] = xp.array([self.__w2v(i) for i in data["text"]])
        return train_data

    def __w2v(self, word):
        try:
            vec = self.__model[word]
        except KeyError:
            vec = xp.zeros((UNIT,))
        return vec

    def __get_label_dict(self, train_data):
        label = list(set(i["label"] for i in train_data))
        label.sort()
        lab_dic = {v:i for i,v in enumerate(label)}
        return lab_dic

    def save(self, path):
        with open(path, mode='wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, mode='rb') as f:
            model = pickle.load(f)
        return model

if __name__ == '__main__':
    # make data
    mtd = MakeTrainData(MODEL_PATH, WAKATI_PATH)
    mtd.init_set()
    mtd.save(TRAIN_DATA_PATH)
