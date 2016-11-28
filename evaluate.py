# -*- coding: utf-8 -*-


import os
import pickle

from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from util.constants import *
from util.functions import check_directory
from util.functions import trace


def load_pickle(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
    return data


if __name__ == '__main__':

    report_list = []
    data_path_list = [W2V_MECAB_VEC_DIR, W2V_JUMAN_VEC_DIR,
                      FST_MECAB_VEC_DIR, FST_JUMAN_VEC_DIR]
    clf_path_list = [LR_W2V_MECAB_CLF, LR_W2V_JUMAN_CLF,
                     LR_FST_MECAB_CLF, LR_FST_JUMAN_CLF]

    trace("check directory")
    check_directory(clf_path_list)

    for data_path, clf_path in zip(data_path_list, clf_path_list):
        trace("load", data_path)
        dataset = []
        lab_set = []
        for i, c in enumerate(CATEGORY):
            trace("load", c)
            data = load_pickle(data_path + c)
            label = [i for d in range(len(data))]
            dataset.extend(data)
            lab_set.extend(label)
        trace("divide dateset")
        train_x, test_x, train_t, test_t = train_test_split(dataset, lab_set)

        if os.path.exists(clf_path):
            trace("load LR clf")
            clf = joblib.load(clf_path)
        else:
            trace("training LR")
            clf = LogisticRegressionCV()
            clf.fit(train_x, train_t)
            trace("save model")
            joblib.dump(clf, clf_path)

        trace("LR predict")
        pred = clf.predict(test_x)
        report = classification_report(test_t, pred)
        report_list.append(report)
        trace("accuracy", accuracy_score(test_t, pred))

    for repo, path in zip(report_list, clf_path_list):
        trace(path)
        trace("report\n", repo)

    trace("finish!")
