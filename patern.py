# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re

def find_class(file):
    class_name = re.compile("class (.*):")
    name = re.findall(class_name, file)
    return name
