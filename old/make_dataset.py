# -*- coding: utf-8 -*-


import sys
import pickle


#WAKATI_PATH     = "./data/wakati/mini_data.txt"
WAKATI_PATH     = "./data/wakati/wakati.txt"
#DATASET_PATH    = "./data/train_dataset/livedoor_mini.pkl"
DATASET_PATH    = "./data/train_dataset/livedoor.pkl"
META_SPLIT      = "<hogefugapiyo>"

class MakeDataset():

    def __init__(self, wakati_path):
        self.wakati_path = wakati_path

    def init_set(self):
        self.__train_data = self.__read_doc(self.wakati_path)
        self.__label_dict = self.__get_label_dict(self.__train_data)
        self.__train_data = self.__replace_label(self.__train_data, self.__label_dict)

    def get_train_data(self):
        return self.__train_data

    def __read_doc(self, path):
        train_data  = []
        with open(path, mode='r') as f:
            for line in f:
                no, lab, txt = str(line).split(META_SPLIT)
                one = {"id":no, "label":lab, "text":txt.split()}
                train_data.append(one)
        max_h = max(len(i["text"]) for i in train_data)
        train_data = self.__padding(train_data, max_h)
        return train_data

    def __padding(self, train_data, max_h):
        for i, data in enumerate(train_data):
            pad_txt = ['<pad>' for i in range(max_h - len(data["text"]))]
            train_data[i]["text"] += pad_txt
        return train_data

    def __get_label_dict(self, train_data):
        label = list(set(i["label"] for i in train_data))
        label.sort()
        lab_dic = {v:i for i,v in enumerate(label)}
        return lab_dic

    def __replace_label(self, train_data, label_dict):
        for data in train_data:
            data["label"] = label_dict[data["label"]]
        return train_data

    def save(self, path):
        with open(path, mode='wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, mode='rb') as f:
            model = pickle.load(f)
        return model

if __name__ == '__main__':
    docs = MakeDataset(WAKATI_PATH)
    docs.init_set()
    docs.save(DATASET_PATH)
