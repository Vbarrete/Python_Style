# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os, sys
from patern import *

def style_var(name, file):
    style_name = ""
    #TO DO
    return file.replace(name, style_name)

def style_class(name, file):
    style_name = ""
    split = name.split("_")
    for i in split:
        style_name += i[0].upper()
    return file.replace(name, style_name)

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

class_name = find_class(l_file)
for i in class_name:
    for j in l_file:
        j = style_class(i, j)

var_name = find_var(l_file)
for i in var_name:
    for j in l_file:
        j = style_var(i, j)
