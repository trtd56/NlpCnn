# -*- coding: utf-8 -*-


import os, pickle, codecs
import MeCab
from gensim.models import word2vec
import numpy as np

from util.functions import trace, check_directory


UNIT       = 200
TEXT_DIR   = "./data/text/"
CATEGORY   = {0:"dokujo-tsushin", 1:"it-life-hack", 2:"kaden-channel", 3:"livedoor-homme", 4:"movie-enter",
              5:"peachy",6:"smax",7:"sports-watch",8:"topic-news"}
MODEL_PATH = "./data/model/w2v_model_" + str(UNIT)
DATA_PATH  = "./data/train_data/w2v_data/"


def get_text_path_list(dir_path, category):
    text_dir = os.listdir(dir_path+category)
    path_list = []
    for files in text_dir:
        path_list.append(dir_path+category+"/"+files)
    return path_list

def get_vector(path, model):
    tagger = MeCab.Tagger("-Owakati")
    text = codecs.open(path,"r","utf-8").readlines()[2:] # Delete URL & date
    vec_list = []
    for line in text:
        line = line.replace("\n","")
        if not len(line) == 0:
            text_sp = tagger.parse(line)
            text_sp = text_sp.split()
            if not len(text_sp) == 0:
                try:
                    vec = np.array([model[word] for word in text_sp])
                    vec = vec.mean(axis=0)
                    vec_list.append(vec)
                except KeyError:
                    pass
    return vec_list

def make_train_data(model, text_dir, data_path, category):
    for i, c in category.items():
        path_list = get_text_path_list(text_dir, c)
        feature = []
        for p in path_list:
            trace("infer", p)
            vec_list = get_vector(p, model)
            if not len(vec_list) == 0:
                feature.extend(vec_list)
        trace("save ", c)
        save_pickle(data_path+c,feature)

def save_pickle(path, data):
    with open(path, mode='wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    model = word2vec.Word2Vec.load(MODEL_PATH)
    check_directory([DATA_PATH])
    make_train_data(model, TEXT_DIR, DATA_PATH, CATEGORY)
