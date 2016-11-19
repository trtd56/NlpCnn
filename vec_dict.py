# -*- coding: utf-8 -*-

import pickle

import numpy
from gensim.models import word2vec
from chainer import cuda

from make_dataset import MakeDataset
from functions import trace

DATASET_PATH    = "./data/train_dataset/livedoor.pkl"
#DATASET_PATH    = "./data/train_dataset/livedoor_mini.pkl"
VEC_DATA_PATH   = "./data/train_dataset/w2v_dict.pkl"
#VEC_DATA_PATH   = "./data/train_dataset/w2v_dict_mini.pkl"

MODEL_PATH      = "./data/model/w2v_model_all"
UNIT            = 200
GPU             = -1
SEED            = 123

xp = cuda.cupy if GPU >= 0 else numpy
xp.random.seed(SEED)

class VecDict():

    def __init__(self, model_path, dataset):
        self.__model   = word2vec.Word2Vec.load(model_path)
        self.__dataset = dataset
        self.__label   = None
        self.__vec     = None

    def infer(self):
        self.__label = self.__get_label_data(self.__dataset)
        self.__vec   = self.__get_vector(self.__dataset)

    def __get_label_data(self, train_data):
        label = list(set(i["label"] for i in train_data))
        label.sort()
        lab_dic = {v:i for i,v in enumerate(label)}
        label = [lab_dic[i["label"]] for i in train_data]
        return label

    def get_train_data(self):
        f_size = self.__vec.shape[1]*self.__vec.shape[2]
        vec = self.__vec.reshape((-1, f_size))
        return self.__label, vec

    def __get_vector(self, train_data):
        vec_list = []
        leng = len(train_data)
        num = 0
        for data in train_data:
            num += 1
            trace(num, "/", leng)
            vec = xp.array([self.__w2v(i) for i in data["text"]])
            vec_list.append(vec)
        return xp.array(vec_list)

    def __w2v(self, word):
        try:
            return self.__model[word]
        except KeyError:
            return xp.zeros((UNIT,))

    def save(self, path):
        with open(path, mode='wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, mode='rb') as f:
            model = pickle.load(f)
        return model

if __name__ == '__main__':
    trace("load train dataset")
    dset = MakeDataset.load(DATASET_PATH)
    dataset = dset.get_train_data()
    trace("finish!")

    trace("infer vector")
    vec_dict = VecDict(MODEL_PATH, dataset)
    vec_dict.infer()
    vec_dict.save(VEC_DATA_PATH)
    trace("finish!")
