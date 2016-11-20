# -*- coding: utf-8 -*

import os, sys
import MeCab
import random

SEED            = 0
META_SPLIT      = "<hogefugapiyo>"
TEXT_DIR_PATH   = "./data/text/"
TEST_PATH       = "./data/wakati/test.txt"
TRAIN_PATH      = "./data/wakati/train.txt"
TRAIN_W2V_PATH  = "./data/wakati/train_w2v.txt"
WAKATI_PATH     = "./data/wakati/wakati.txt"
WAKATI_W2V_PATH = "./data/wakati/wakati_w2v.txt"

def get_text_file_path(text_dir_path):
    text_dir = os.listdir(text_dir_path)
    path_list = []
    for files in text_dir:
        try:
            file_list = os.listdir(text_dir_path+files)
            for f in file_list:
                full_path = text_dir_path + files + "/" + f
                path_list.append((files, full_path))
        except NotADirectoryError:
            pass
    return path_list

def divide_test_train(path_list):
    leng = len(path_list)
    index = random.sample(range(leng),leng)
    test  = path_list[:int(leng/20)]
    train = path_list[int(leng/20):]
    return test, train

def wakati_text(tag, path, label):
    tagger = MeCab.Tagger("-Owakati")
    out = ""
    for line in open(path, 'r'):
        line = line.replace("\n","")
        if not len(line) == 0:
            text_sp = tagger.parse(line)
            if label:
                text_sp = tag + META_SPLIT + text_sp
            if is_id:
                text_sp = "{0:06d}".format(num) + META_SPLIT + text_sp
            out += text_sp
    return out

def write_wakati(path_list, out_path, label=True):
    out = ""
    for data in path_list:
        tag, path = data
        out += wakati_text(tag, path, label, is_id)
    with open(out_path, "a") as f:
        f.write(out)

def make_all_wakati_data(path_list, out_path, label=True):
    tagger = MeCab.Tagger("-Owakati")
    num = 0
    out = ""
    for data in path_list:
        tag, path = data
        for line in open(path, 'r'):
            line = line.replace("\n","")
            if not len(line) == 0:
                num += 1
                text_sp = tagger.parse(line)
                if label:
                    text_sp =  "{0:06d}".format(num) + META_SPLIT + tag + META_SPLIT + text_sp
                out += text_sp
    with open(out_path, "a") as f:
        f.write(out)


if __name__ == '__main__':

    random.seed(SEED)
    path_list = get_text_file_path(TEXT_DIR_PATH)
    test, train = divide_test_train(path_list)
    write_wakati(test, TEST_PATH)
    write_wakati(train, TRAIN_PATH)
    write_wakati(train, TRAIN_W2V_PATH, label=False)
    make_all_wakati_data(path_list, WAKATI_PATH)
    make_all_wakati_data(path_list, WAKATI_W2V_PATH, label=False)
