# -*- coding: utf-8 -*-

import codecs
import os

from util.constants import *
from util.functions import check_directory
from util.functions import get_text_file_path
from util.functions import trace
from util.functions import wakati
from util.functions import write_file


def wakati_all_text(path_list, mode):
    leng = len(path_list) - 1
    out = ""
    for i, path in enumerate(path_list):
        trace(mode, "wakati", i, "/", leng)
        out += wakati(path, mode)
    return out



if __name__ == '__main__':

    trace("check directory")
    dir_path = [WAKATI_MECAB, WAKATI_JUMAN]
    check_directory(dir_path)

    trace("read text file")
    path_list = get_text_file_path(CORPUS_DIR)

    trace("wakati mecab")
    wakati_mecab = wakati_all_text(path_list, "mecab")
    trace("wakati juman")
    wakati_juman = wakati_all_text(path_list, "juman")

    trace("save wakati file")
    write_file(WAKATI_MECAB, wakati_mecab)
    write_file(WAKATI_JUMAN, wakati_juman)

    trace("finish!")
