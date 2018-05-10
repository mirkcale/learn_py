#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fpath = './Animal.py'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
    f.close()