# -*- coding: utf-8 -*-


import os, pickle
import numpy as np

from sklearn.linear_model import LogisticRegressionCV
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib

from util.functions import trace, check_directory
from util.cinstants import *


def load_pickle(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
    return data


if __name__ == '__main__':

    report_list = []
    data_path_list = [W2V_MECAB_VEC_DIR, W2V_JUMAN_VEC_DIR, FST_MECAB_VEC_DIR, FST_JUMAN_VEC_DIR]
    clf_path_list  = [LR_W2V_MECAB_CLF, LR_W2V_JUMAN_CLF, LR_FST_MECAB_CLF, LR_FST_JUMAN_CLF]

    trace("check directory")
    check_directory(clf_path_list)

    for data_path, clf_path in zip(data_path_list, clf_path_list):
        trace("load", data_path)
        dataset = []
        lab_set = []
        for i, c in CATEGORY.items():
            trace("load", c)
            data = load_pickle(data_path+c)
            label = [i for d in range(len(data))]
            dataset.extend(data)
            lab_set.extend(label)
        trace("divide dateset")
        train_x, test_x, train_t, test_t = train_test_split(dataset, lab_set)


        trace("training LR")
        clf  = LogisticRegressionCV()
        clf.fit(train_x, train_t)
        trace("LR predict")
        pred = lr.predict(test_x)
        report = classification_report(test_t, pred)
        trace("accuracy",accuracy_score(test_t, pred))

        trace("save model")
        joblib.dump(lr, clf_path)
        report_list.append(report)

    for repo, path in zip(report_list, clf_path_list):
        trace(path)
        trace("report\n",r)

    trace("finish!")
