# -*- coding: utf-8 -*-

import codecs
import MeCab
from pyknp import Jumanpp
from gensim.models import word2vec
from multiprocessing import Pool
from multiprocessing import Process

from util.constants import *
from util.functions import trace
from util.functions import check_directory
from util.functions import replace_head2jumanpp
from util.functions import write_file


MECAB_SEP = MeCab.Tagger("-Owakati")
JUMAN_SEP = Jumanpp()

def read_jawiki(path):
    docs  = []
    for line in open(path, 'r', encoding='utf-8'):
        if "<abstract>" and "。" in line and len(line) > JAWIKI_MIN_COUNT:
            line = line.replace("</abstract>","")
            line = line.replace("<abstract>","")
            line = replace_head2jumanpp(line)
            if not len(line) == 0:
                docs.append(line)
    return docs

def split_mecab(line):
        return MECAB_SEP.parse(line)

def split_juman(line):
        line = line.replace("\n", "")
        trace(line)
        text_sp = JUMAN_SEP.analysis(line)
        text_sp = " ".join([i.midasi for i in text_sp.mrph_list()]) + "\n"
        return text_sp

def multi(func, data):
        p = Pool(MULTI)
        result = p.map(func, data)
        return result

def bind(data):
    out = ""
    for i in data:
        out += i
    return out


if __name__ == '__main__':

    trace("check directory")
    dir_path = [WAKATI_MECAB_WIKI, WAKATI_JUMAN_WIKI, W2V_MECAB_MODEL_WIKI, W2V_JUMAN_MODEL_WIKI]
    check_directory(dir_path)

    trace("read jawiki file")
    docs = read_jawiki(JAWIKI_XML_PATH)

    trace("--- mecab ---")
    trace("wakati")
    wakati_mecab = multi(split_mecab, docs)
    trace("bind")
    wakati_mecab = bind(wakati_mecab)
    trace("save")
    write_file(WAKATI_MECAB_WIKI, wakati_mecab)

    trace("--- juman ---")
    trace("wakati")
    wakati_juman = multi(split_juman, docs)
    trace("bind")
    wakati_juman = bind(wakati_juman)
    trace("save")
    write_file(WAKATI_JUMAN_WIKI, wakati_juman)

    trace("load mecab wakati file")
    data = word2vec.Text8Corpus(WAKATI_MECAB_WIKI)
    trace("train mecab word2vec")
    model = word2vec.Word2Vec(data, size=UNIT)
    trace("save mecab word2vec model")
    model.save(W2V_MECAB_MODEL_WIKI)

    trace("load juman wakati file")
    data = word2vec.Text8Corpus(WAKATI_JUMAN_WIKI)
    trace("train juman word2vec")
    model = word2vec.Word2Vec(data, size=UNIT)
    trace("save juman word2vec model")
    model.save(W2V_JUMAN_MODEL_WIKI)

    trace("finish!")
