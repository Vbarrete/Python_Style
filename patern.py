# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re

def find_class(files):
    class_name = re.compile("class (.*):")
    name = []
    for i in files:
        name += re.findall(class_name, i)
    return name
