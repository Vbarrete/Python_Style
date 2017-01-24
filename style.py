# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os, sys
from patern import *

l_file = []
if len(sys.argv) == 1:
    print("Invalide Argument")
    exit()
for i in range(1, len(sys.argv)-1):
    try:
        fd = open(i, "r")
    except:
        print("Invalide Argument")
        exit()
    l_file.append(fd.read())
    fd.close()

find_class_name(l_file)
