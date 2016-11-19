# -*- coding: utf-8 -*-

from datetime import datetime

def trace(*args):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    x = " ".join([str(i) for i in args])
    print(now+".... "+x, flush=True)
