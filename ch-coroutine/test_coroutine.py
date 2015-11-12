# -*- coding: utf-8 -*-
__author__ = 'PCPC'


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s...' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[producer] producing %s..' % n)
        r = c.send(n)
        print('[producer] Consumer return %s ' % r)
    c.close()


c = consumer()
produce(c)
