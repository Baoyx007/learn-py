__author__ = 'haven'

from io import StringIO

f = StringIO()
f.write('hello')
print(f.getvalue())
