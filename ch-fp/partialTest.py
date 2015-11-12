import functools
# -*- coding: utf-8 -*-
__author__ = 'PCPC'

int2 = functools.partial(int,base=2)
print(int2('101010101'))
