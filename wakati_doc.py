# -*- coding: utf-8 -*


import os
import MeCab

from util.functions import trace


TEXT_DIR   = "./data/text/"
WAKATI_DIR = "./data/wakati/"


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

def write_file(out_path, wakati):
    if not os.path.isdir(out_path):
        os.makedirs(out_path)
    with open(out_path+"wakati.txt", "w") as f:
        f.write(wakati)


if __name__ == '__main__':

    path_list = get_text_file_path(TEXT_DIR)
    wakati    = wakati_all_text(path_list)
    write_file(WAKATI_DIR, wakati)
