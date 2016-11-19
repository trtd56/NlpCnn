# -*- coding: utf-8 -*-


from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib


from functions import trace
from vec_dict import VecDict


#VEC_DICT_PATH    = "./data/train_dataset/w2v_dict.pkl"
VEC_DICT_PATH    = "./data/train_dataset/w2v_dict_mini.pkl"

SVM_MODEL = "./data/model/svm_mini.pkl"

if __name__ == '__main__':
    # make data
    trace("load train dataset")
    vec_dict = VecDict.load(VEC_DICT_PATH)
    lab, vec = vec_dict.get_train_data()
    trace("finish!")

    data_train, data_test, label_train, label_test = train_test_split(vec, lab)

    # train
    clf = svm.SVC()
    clf.fit(data_train, label_train)

    ## test
    pred = clf.predict(data_test)
    print(classification_report(label_test, pred))
    print(accuracy_score(label_test, pred))
    joblib.dump(clf, SVM_MODEL)
    trace("save model")
