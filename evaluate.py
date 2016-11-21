# -*- coding: utf-8 -*-


import os, pickle
import numpy as np

from sklearn.linear_model import LogisticRegressionCV
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib

from util.functions import trace, check_directory



DATA_PATH = "./data/train_data/w2v_data/"
CATEGORY   = {0:"dokujo-tsushin", 1:"it-life-hack", 2:"kaden-channel", 3:"livedoor-homme", 4:"movie-enter",
              5:"peachy",6:"smax",7:"sports-watch",8:"topic-news"}
CLF_MODEL = "./data/model/w2v_lr_model"


def load_pickle(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
    return data

if __name__ == '__main__':
    trace("load train data")
    dataset = []
    lab_set = []
    for i, c in CATEGORY.items():
        trace("load", c)
        data = load_pickle(DATA_PATH+c)
        label = [i for d in range(len(data))]
        dataset.extend(data)
        lab_set.extend(label)
    trace("divide dateset")
    train_x, test_x, train_t, test_t = train_test_split(dataset, lab_set)

    clf = LogisticRegressionCV()
    trace("training data")
    clf.fit(train_x, train_t)

    trace("predict")
    pred = clf.predict(test_x)
    report = classification_report(test_t, pred)
    score = accuracy_score(test_t, pred)
    trace("report\n",report)
    trace("accuracy", score)


    trace("save model")
    joblib.dump(clf, CLF_MODEL)
    trace("finish!")
