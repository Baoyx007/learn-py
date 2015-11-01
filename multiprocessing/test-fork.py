__author__ = 'haven'
import os,time
from multiprocessing import Process
print('process (%s) start..'%os.getpid())

def run_proc(name):
    print('RUn child process %s (%s)...'%(name,os.getpid()))


if __name__=='__main__':
    print('parent process %s'%os.getpid())
    p = Process(target=run_proc,args=('test',))
    p.start()
    p.join()
    print('child end')
'''
pid = os.fork()
if pid==0:
    print('i am child process (%s) and my parent is %s'%(os.getpid(),os.getppid()))
else:
    print('i(%s) just created a child process (%s)'%(os.getpid(),pid))
'''
# time.sleep(100)

# time.sleep(100)
