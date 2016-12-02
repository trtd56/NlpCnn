# -*- coding: utf-8 -*-

import os, codecs
from datetime import datetime
import MeCab
from pyknp import Jumanpp

MECAB_SEP = MeCab.Tagger("-Owakati")
JUMAN_SEP = Jumanpp()

def trace(*args):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    x = " ".join([str(i) for i in args])
    print(now+" ... "+x)

def check_directory(path_list):
    for path in path_list:
        sp_path = path.split("/")
        sp_path.pop()
        dir_path = "/".join(sp_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

def get_text_file_path(text_dir_path):
    text_dir = os.listdir(text_dir_path)
    path_list = []
    for files in text_dir:
        try:
            file_list = os.listdir(text_dir_path + files)
            for f in file_list:
                full_path = text_dir_path + files + "/" + f
                path_list.append(full_path)
        except NotADirectoryError:
            pass
    return path_list

def wakati(path, mode):
    out = ""
    text = codecs.open(path,"r","utf-8").readlines()[2:] # Delete URL & date
    for line in text:
        # replace unused words
        line = line.replace("\n","")
        if mode == "mecab":
            if not len(line) == 0:
                text_sp = MECAB_SEP.parse(line)
                out += text_sp
        elif mode == "juman":
            line = replace_head2jumanpp(line)
            if not len(line) == 0:
                trace("juman",line)
                text_sp = JUMAN_SEP.analysis(line)
                text_sp = " ".join([i.midasi for i in text_sp.mrph_list()]) + "\n"
                out += text_sp
    return out

def replace_head2jumanpp(line):
    line = line.replace(" ","")
    line = line.replace("@","")
    line = line.replace("#","")
    return line
