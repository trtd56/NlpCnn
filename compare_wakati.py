# -*- coding: utf-8 -*-

import random
import codecs
import MeCab
from pyknp import Jumanpp

from util.constants import *
from util.functions import trace
from util.functions import get_text_file_path
from util.functions import replace_head2jumanpp

MECAB_SEP = MeCab.Tagger("-Owakati")
JUMAN_SEP = Jumanpp()

def wakati_2_method(path):
    text = codecs.open(path,"r","utf-8").readlines()[2:] # Delete URL & date
    text = [i.replace("\n","") for i in text if not i == "\n"]
    text = [i for i in text if len(i) > 10]
    samp_line = random.sample(text,1)[0]
    mecab_sp = MECAB_SEP.parse(samp_line)
    mecab_sp = "/".join(mecab_sp.split())
    juman_sp = JUMAN_SEP.analysis(replace_head2jumanpp(samp_line))
    juman_sp = "/".join([i.midasi for i in juman_sp.mrph_list()])
    print()
    print("=== path ===")
    print(path)
    print()
    print("=== mecab split ===")
    print(mecab_sp)
    print()
    print("=== juman split ===")
    print(juman_sp)
    print()
    print("--------------------------------------------------------------")

if __name__ == '__main__':

    random.seed(SEED)

    trace("read text file")
    path_list = get_text_file_path(CORPUS_DIR)
    samp_path = random.sample(path_list, 100)
    for path in samp_path:
        wakati_2_method(path)
