__author__ = 'haven'
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr

msg = MIMEText('hello,send by python','plain','utf-8')

from_addr = input('from:')
pwd = input('pwd:')
to_addr = input('to:')
smtp_server = input('SMTP server:')

def _format_addr(s):
    name ,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


msg['From']=_format_addr('python爱好者 <%s>'%from_addr)
msg['To']=_format_addr('管理员 <%s>'%to_addr)
msg['Subject']=Header('from smtp ','utf-8').encode()


import smtplib
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,pwd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()



