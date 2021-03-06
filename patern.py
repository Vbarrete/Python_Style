# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re

def find_var(files, class_name):
    var_name = re.compile("(.*) =[^=]")
    name = []
    for i in files:
        name += re.findall(var_name, i)
    return name

def find_class(files):
    class_name = re.compile("class (.*):")
    name = []
    for i in files:
        name += re.findall(class_name, i)
    return name
