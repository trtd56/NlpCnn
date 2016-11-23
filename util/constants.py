UNIT              = 200

DATA_ROOT         = "./data/"

CORPUS_DIR        = DATA_ROOT + "text/"
CATEGORY          = ["dokujo-tsushin", "it-life-hack", "kaden-channel", "livedoor-homme", "movie-enter",
                     "peachy", "smax", "sports-watch", "topic-news"]

WAKATI_MECAB      = DATA_ROOT + "wakati/wakati_mecab.txt"
WAKATI_JUMAN      = DATA_ROOT + "wakati/wakati_juman.txt"

W2V_MECAB_MODEL   = DATA_ROOT + "model/w2v_mecab_model"
W2V_JUMAN_MODEL   = DATA_ROOT + "model/w2v_juman_model"
FST_MECAB_MODEL   = DATA_ROOT + "model/fst_mecab_model.vec"
FST_JUMAN_MODEL   = DATA_ROOT + "model/fst_juman_model.vec"

W2V_MECAB_VEC_DIR = DATA_ROOT + "vec/w2v_mecab/"
W2V_JUMAN_VEC_DIR = DATA_ROOT + "vec/w2v_juman/"
FST_MECAB_VEC_DIR = DATA_ROOT + "vec/fst_mecab/"
FST_JUMAN_VEC_DIR = DATA_ROOT + "vec/fst_juman/"

LR_W2V_MECAB_CLF  = DATA_ROOT + "clf/lr_w2v_mecab_clf"
LR_W2V_JUMAN_CLF  = DATA_ROOT + "clf/lr_w2v_juman_clf"
LR_FST_MECAB_CLF  = DATA_ROOT + "clf/lr_fst_mecab_clf"
LR_FST_JUMAN_CLF  = DATA_ROOT + "clf/lr_fst_juman_clf"
