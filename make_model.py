# -*- coding: utf-8 -*


import os
import MeCab
from gensim.models import word2vec

from util.functions import trace, check_directory


UNIT        = 200

TEXT_DIR    = "./data/text/"
WAKATI_PATH = "./data/wakati/wakati.txt"
MODEL_PATH  = "./data/model/w2v_model_" + str(UNIT)


def get_text_file_path(text_dir_path):
    text_dir = os.listdir(text_dir_path)
    path_list = []
    for files in text_dir:
        try:
            file_list = os.listdir(text_dir_path+files)
            for f in file_list:
                full_path = text_dir_path + files + "/" + f
                path_list.append(full_path)
        except NotADirectoryError:
            pass
    return path_list

def wakati_text(path):
    tagger = MeCab.Tagger("-Owakati")
    out = ""
    for line in open(path, 'r'):
        line = line.replace("\n","")
        if not len(line) == 0:
            text_sp = tagger.parse(line)
            out += text_sp
    return out

def wakati_all_text(path_list):
    leng = len(path_list)
    out = ""
    for i, path in enumerate(path_list):
        trace("wakati", i, "/", leng)
        out += wakati_text(path)
    return out

def write_file(out_path, data):
    with open(out_path, "w") as f:
        f.write(data)

if __name__ == '__main__':

    trace("check directory")
    dir_path = [WAKATI_PATH, MODEL_PATH]
    check_directory(dir_path)

    trace("read text file")
    path_list = get_text_file_path(TEXT_DIR)
    wakati    = wakati_all_text(path_list)
    write_file(WAKATI_PATH, wakati)
    trace("save wakati file")

    trace("load wakati file")
    data = word2vec.Text8Corpus(WAKATI_PATH)
    trace("train word2vec")
    model = word2vec.Word2Vec(data, size=UNIT)
    trace("save word2vec model")
    model.save(MODEL_PATH)
    trace("finish!")
