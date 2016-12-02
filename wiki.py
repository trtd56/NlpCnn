# -*- coding: utf-8 -*-

import MeCab
from pyknp import Jumanpp
import codecs

from util.constants import *
from util.functions import trace
from util.functions import replace_head2jumanpp


def wakati_jawiki(path, mode):
    out  = ""
    for line in open(path, 'r', encoding='utf-8'):
        if "<abstract>" and "。" in line and len(line) > JAWIKI_MIN_COUNT:
            line= codecs.getwriter('utf_8')(line)
            #line = line.encode("utf-8")
            trace(mode,"wakati",line)
            #if mode == "mecab":
            #    if not len(line) == 0:
            #        text_sp = MECAB_SEP.parse(line)
            #        out += text_sp
            #elif mode == "juman":
            #    line = replace_head2jumanpp(line)
            #    if not len(line) == 0:
            #        trace("juman",line)
            #        text_sp = JUMAN_SEP.analysis(line)
            #        text_sp = " ".join([i.midasi for i in text_sp.mrph_list()]) + "\n"
            #        out += text_sp
    return out


if __name__ == '__main__':

    trace("check directory")

    trace("read jawiki")
    wakati = wakati_jawiki(JAWIKI_XML_PATH, "mecab")
    wakati = wakati_jawiki(JAWIKI_XML_PATH, "juman")
