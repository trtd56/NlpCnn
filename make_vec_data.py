# -*- coding: utf-8 -*-


import os, pickle, codecs
import MeCab
from pyknp import Jumanpp
from gensim.models import word2vec
import numpy as np

from util.functions import trace, check_directory
from util.cinstants import *

Tagger  = MeCab.Tagger("-Owakati")
Jumanpp = Jumanpp()

def get_text_path_list(dir_path, category):
    text_dir = os.listdir(dir_path+category)
    path_list = []
    for files in text_dir:
        path_list.append(dir_path+category+"/"+files)
    return path_list

def get_vector(path, model, mode):
    text = codecs.open(path,"r","utf-8").readlines()[2:] # Delete URL & date
    vec_list = []
    for line in text:
        line = line.replace("\n","")
        if not len(line) == 0:
            if mode == "mecab":
                text_sp = Tagger.parse(line)
                text_sp = text_sp.split()
            elif mode == "juman":
                try:
                    text_sp = Jumanpp.analysis(line)
                    text_sp = " ".join([i.midasi for i in text_sp.mrph_list()])
                except ValueError:
                    text_sp = []
            if not len(text_sp) == 0:
                try:
                    vec = np.array([model[word] for word in text_sp])
                    vec = vec.mean(axis=0)
                    vec_list.append(vec)
                except KeyError:
                    pass
    return vec_list

def make_train_data(model, text_dir, data_path, category, mode):
    for i, c in category.items():
        path_list = get_text_path_list(text_dir, c)
        feature = []
        for p in path_list:
            trace(mode,"infer", p)
            vec_list = get_vector(p, model, mode)
            if not len(vec_list) == 0:
                feature.extend(vec_list)
        trace("save ", c)
        save_pickle(data_path+c,feature)

def save_pickle(path, data):
    with open(path, mode='wb') as f:
        pickle.dump(data, f)

def load_fst_words_vector(path):
    vectors = {}
    with open(path, "r", encoding="utf-8") as vec:
        for i, line in enumerate(vec):
            try:
                elements = line.strip().split()
                word = elements[0]
                vec = np.array(elements[1:], dtype=float)
                if not word in vectors and len(vec) >= 100:
                    # ignore the case that vector size is invalid
                    vectors[word] = vec
            except ValueError:
                continue
            except UnicodeDecodeError:
                continue
        return vectors


if __name__ == '__main__':
    trace("check directory")
    dir_path = [W2V_MECAB_VEC_DIR, W2V_JUMAN_VEC_DIR, FST_MECAB_VEC_DIR, FST_JUMAN_VEC_DIR]
    check_directory(dir_path)

    trace("make mecab word2vec train data")
    w2v_model = word2vec.Word2Vec.load(W2V_MECAB_MODEL)
    make_train_data(w2v_model, CORPUS_DIR, W2V_MECAB_VEC_DIR, CATEGORY, "mecab")

    trace("make juman word2vec train data")
    w2v_model = word2vec.Word2Vec.load(W2V_JUMAN_MODEL)
    make_train_data(w2v_model, CORPUS_DIR, W2V_JUMAN_VEC_DIR, CATEGORY, "juman")

    trace("make mecab fasttext train data")
    fst_model = load_fst_words_vector(FST_MECAB_MODEL)
    make_train_data(fst_model, CORPUS_DIR, FST_MECAB_VEC_DIR, CATEGORY, "mecab")

    trace("make juman fasttext train data")
    fst_model = load_fst_words_vector(FST_JUMAN_MODEL)
    make_train_data(fst_model, CORPUS_DIR, FST_JUMAN_VEC_DIR, CATEGORY, "juman")

    trace("finish!")
