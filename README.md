# TODO

- download livedoor news corpus

~~~bash
$ wget http://www.rondhuit.com/download/ldcc-20140209.tar.gz
$ tar xvzf ldcc-20140209.tar.gz
$ mkdir data && mv text/ data/
~~~

- environment

~~~bash
$ docker pull trtd56/nlp-python
~~~

- file path setting

~~~bash
$ vim util/constants.py
~~~

- exec

~~~bash
$ python wakati.py
$ python train_w2v_model.py
$ fasttext {mecab wakati file path}
$ fasttext {juman++ wakati file path}
$ python make_vec_data.py
$ python -u evaluate.py > result
~~~

