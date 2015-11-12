# -*- coding:utf-8 -*-
__author__ = 'haven'
import sqlite3


def create_user():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # cursor.execute("create table user(id VARCHAR (20) PRIMARY KEY ,NAME VARCHAR (20))")
    cursor.execute("insert INTO USER (id,NAME) VALUEs ('2','jack')")
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()


# create_user()
def select_user():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM USER")
    print(list(map(lambda x:x[0],cursor.fetchall())))
    cursor.close()
    conn.commit()
    conn.close()

# select_user()

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine('sqlite:///test.db')
DBSession = sessionmaker(bind=engine)

session = DBSession()
# new_user = User(id='5',name='bob')
# session.add(new_user)
user = session.query(User).filter(User.id=='5').one()
print(user,user.name,type(user))
# session.commit()
session.close()