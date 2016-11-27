# -*- coding: utf-8 -*-


import os, codecs

from util.functions import trace, check_directory, wakati
from util.constants import *


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

def wakati_all_text(path_list, mode):
    leng = len(path_list) - 1
    out = ""
    for i, path in enumerate(path_list):
        trace(mode,"wakati", i, "/", leng)
        out += wakati(path, mode)
    return out

def write_file(out_path, data):
    with codecs.open(out_path, "w", 'utf-8') as f:
        f.write(data)

if __name__ == '__main__':

    trace("check directory")
    dir_path = [WAKATI_MECAB, WAKATI_JUMAN]
    check_directory(dir_path)

    trace("read text file")
    path_list     = get_text_file_path(CORPUS_DIR)

    trace("wakati mecab")
    wakati_mecab  = wakati_all_text(path_list, "mecab")
    trace("wakati juman")
    wakati_juman  = wakati_all_text(path_list, "juman")

    trace("save wakati file")
    write_file(WAKATI_MECAB, wakati_mecab)
    write_file(WAKATI_JUMAN, wakati_juman)

    trace("finish!")
