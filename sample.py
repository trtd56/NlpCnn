# coding: utf-8
import os,codecs,re,pickle
import numpy as np
from gensim.models import word2vec
from gensim import matutils


basepath="./data/text"
dir_names=["dokujo-tsushin","it-life-hack","kaden-channel","livedoor-homme","movie-enter","peachy","smax","sports-watch","topic-news"]

def make_data(model_filename,data_filename,tokenize):
    model=word2vec.Word2Vec.load(model_filename)
    X=[]
    y=[]
    for category,dir_name in enumerate(dir_names):
        dir_name=os.path.join(basepath,dir_name)
        for filename in os.listdir(dir_name):
            filename=os.path.join(dir_name,filename)
            text=codecs.open(filename,"r","utf-8").readlines()[2:] # for removing the date (1st line)
            text=u"".join(text)
            this_vector=np.array([matutils.unitvec(model[word]) for word in tokenize(text) if word in model]).mean(axis=0)
            X.append(this_vector)
            y.append(category)
    X=np.array(X)
    y=np.array(y)
    data={"data":X,"target":y}
    pickle.dump(data,open(data_filename,"wb"))

def evaluate(data_filename,classifier,n_runs=30,verbose=False):
    data=pickle.load(open(data_filename))
    X=data["data"]
    y=data["target"]
    ntr=np.int32(len(y)*0.7)
    accuracies=np.zeros(n_runs)
    for i in xrange(n_runs):
        idx=np.random.permutation(len(y))
        itr=idx[:ntr]
        ite=idx[ntr:]
        classifier.fit(X[itr],y[itr])
        accuracy=classifier.score(X[ite],y[ite])
        if verbose:
            print("accuracy:",accuracy)
        accuracies[i]=accuracy
    return accuracies

if __name__ == '__main__':
    make_data("/path/to/w2v_model",
              "data.pkl",
              tokenize)
    from sklearn.linear_model import LogisticRegressionCV
    accuracies=evaluate("data.pkl",
                        LogisticRegressionCV(),
                        verbose=True)
print("accuracies: {0}, std: {1}".format(np.mean(accuracies),np.std(accuracies)))
