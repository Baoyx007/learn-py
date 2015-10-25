__author__ = 'haven'
from os import listdir, path
# l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print(l)
f = lambda searchdir, filename: [path.join(searchdir, f) for f in listdir(searchdir) if f == filename]

print(f('.', 'bug_fix.py'))
