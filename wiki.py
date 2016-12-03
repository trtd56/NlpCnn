# -*- coding: utf-8 -*-

import codecs
import MeCab
from pyknp import Jumanpp
from gensim.models import word2vec

from util.constants import *
from util.functions import trace
from util.functions import check_directory
from util.functions import replace_head2jumanpp
from util.functions import write_file


MECAB_SEP = MeCab.Tagger("-Owakati")
JUMAN_SEP = Jumanpp()

def wakati_jawiki(path, mode):
    out  = ""
    count = 0
    for line in open(path, 'r', encoding='utf-8'):
        if "<abstract>" and "。" in line and len(line) > JAWIKI_MIN_COUNT:
            line = line.replace("</abstract>","")
            line = line.replace("<abstract>","")
            count += 1
            trace(mode,"wakati",count)
            if mode == "mecab":
                if not len(line) == 0:
                    text_sp = MECAB_SEP.parse(line)
                    out += text_sp
            elif mode == "juman":
                line = replace_head2jumanpp(line)
                if not len(line) == 0:
                    #trace("juman", line)
                    text_sp = JUMAN_SEP.analysis(line)
                    text_sp = " ".join([i.midasi for i in text_sp.mrph_list()]) + "\n"
                    out += text_sp
    return out


if __name__ == '__main__':

    trace("check directory")
    dir_path = [WAKATI_MECAB_WIKI, WAKATI_JUMAN_WIKI, W2V_MECAB_MODEL_WIKI, W2V_JUMAN_MODEL_WIKI]
    check_directory(dir_path)

    trace("read & wakati jawiki")
    wakati_mecab = wakati_jawiki(JAWIKI_XML_PATH, "mecab")
    write_file(WAKATI_MECAB_WIKI, wakati_mecab)
    wakati_juman = wakati_jawiki(JAWIKI_XML_PATH, "juman")
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
