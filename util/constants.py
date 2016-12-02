SEED                   = 123
UNIT                   = 200

DATA_ROOT              = "./data/"

CORPUS_DIR             = DATA_ROOT + "text/"
CATEGORY               = ["dokujo-tsushin", "it-life-hack", "kaden-channel", "livedoor-homme", "movie-enter",
                          "peachy", "smax", "sports-watch", "topic-news"]
JAWIKI_XML_PATH        = DATA_ROOT + "jawiki/jawiki-latest-abstract.xml"

WAKATI_MECAB           = DATA_ROOT + "wakati/wakati_mecab.txt"
WAKATI_JUMAN           = DATA_ROOT + "wakati/wakati_juman.txt"
WAKATI_MECAB_WIKI      = DATA_ROOT + "wakati/wakati_mecab_wiki.txt"
WAKATI_JUMAN_WIKI      = DATA_ROOT + "wakati/wakati_juman_wiki.txt"

W2V_MECAB_MODEL        = DATA_ROOT + "model/w2v_mecab_model"
W2V_JUMAN_MODEL        = DATA_ROOT + "model/w2v_juman_model"
FST_MECAB_MODEL        = DATA_ROOT + "model/fst_mecab_model.vec"
FST_JUMAN_MODEL        = DATA_ROOT + "model/fst_juman_model.vec"
W2V_MECAB_MODEL_WIKI   = DATA_ROOT + "model/w2v_mecab_model_wiki"
W2V_JUMAN_MODEL_WIKI   = DATA_ROOT + "model/w2v_juman_model_wiki"
FST_MECAB_MODEL_WIKI   = DATA_ROOT + "model/fst_mecab_model_wiki.vec"
FST_JUMAN_MODEL_WIKI   = DATA_ROOT + "model/fst_juman_model_wiki.vec"

W2V_MECAB_VEC_DIR      = DATA_ROOT + "vec/w2v_mecab/"
W2V_JUMAN_VEC_DIR      = DATA_ROOT + "vec/w2v_juman/"
FST_MECAB_VEC_DIR      = DATA_ROOT + "vec/fst_mecab/"
FST_JUMAN_VEC_DIR      = DATA_ROOT + "vec/fst_juman/"
W2V_MECAB_VEC_DIR_WIKI = DATA_ROOT + "vec/w2v_mecab_wiki/"
W2V_JUMAN_VEC_DIR_WIKI = DATA_ROOT + "vec/w2v_juman_wiki/"
FST_MECAB_VEC_DIR_WIKI = DATA_ROOT + "vec/fst_mecab_wiki/"
FST_JUMAN_VEC_DIR_WIKI = DATA_ROOT + "vec/fst_juman_wiki/"

LR_W2V_MECAB_CLF  = DATA_ROOT + "clf/lr_w2v_mecab_clf"
LR_W2V_JUMAN_CLF  = DATA_ROOT + "clf/lr_w2v_juman_clf"
LR_FST_MECAB_CLF  = DATA_ROOT + "clf/lr_fst_mecab_clf"
LR_FST_JUMAN_CLF  = DATA_ROOT + "clf/lr_fst_juman_clf"

JAWIKI_MIN_COUNT  = 9
