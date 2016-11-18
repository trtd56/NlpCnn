# -*- coding: utf-8 -*-


from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib


from make_train_data import MakeTrainData


TRAIN_DATA_PATH = "./data/train_dataset/mecab_w2v.pkl"


if __name__ == '__main__':
    # make data
    mtd = MakeTrainData.load(TRAIN_DATA_PATH)
    lab, vec = mtd.get_train_data()

    #data_train, data_test, label_train, label_test = train_test_split(vec, lab)

    # train
    #clf = svm.SVC()
    #clf.fit(data_train, label_train)

    ## test
    #pred = clf.predict(data_test)
    #joblib.dump(clf, 'clf.pkl')
    #print(classification_report(label_test, pred))
    #print(accuracy_score(label_test, pred))
