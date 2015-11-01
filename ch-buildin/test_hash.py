__author__ = 'haven'
import hashlib

md5 = hashlib.md5()
md5.update('byx100200'.encode('utf-8'))
print(md5.hexdigest())

sha256 = hashlib.sha256()
sha256.update('byx100200'.encode('utf-8'))
print(sha256.hexdigest())

print('byx100200'.encode('utf-8'),'byx100200')