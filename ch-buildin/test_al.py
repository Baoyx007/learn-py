__author__ = 'haven'
from datetime import datetime

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015,5,23,12,43,23)
print(dt,dt.timestamp(),dt.strftime('%a,%b %d %H:%M'))

