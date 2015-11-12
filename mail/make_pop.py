# -*- coding:utf-8 -*-
from email.parser import Parser

__author__ = 'haven'
import poplib

email = input('Email:')
pwd = input('pwd:')
pop3_server = input('pop3 server')

server = poplib.POP3(pop3_server)

server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(pwd)

print('messages: %s Siez:%s'%server.stat())
resp,mails,octets = server.list()

print(mails)

index = len(mails)
resp,lines,octets = server.retr(index)
msg_content=b'\r\n'.join(lines)
msg = Parser().parsestr(msg_content)

server.quit()