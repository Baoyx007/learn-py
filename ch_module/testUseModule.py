__author__ = 'haven'

'a test module'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('hello %s' % args[1])
    else:
        print('too many argument')


if __name__ == '__main__':
    test()
