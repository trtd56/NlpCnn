# -*- coding: utf-8 -*-

import os
from datetime import datetime

def trace(*args):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    x = " ".join([str(i) for i in args])
    print(now+" ... "+x)

def check_directory(path_list):
    for path in path_list:
        sp_path = path.split("/")
        sp_path.pop()
        dir_path = "/".join(sp_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
