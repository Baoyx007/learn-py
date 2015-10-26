import functools
# -*- coding: utf-8 -*-
__author__ = 'PCPC'


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('d-e-2')


now()
print(now)
