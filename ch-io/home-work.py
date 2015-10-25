__author__ = 'haven'
import os


# 利用os模块编写一个能实现dir -l输出的程序。

def simu_dir_l(cur_dir):

    # l = [x for x in os.listdir(cur_dir) if os.path.isdir(os.path.join(os.path.abspath(cur_dir), x))]
    # print(l)
    ab_dir_path = os.path.abspath(cur_dir)
    for x in os.listdir(cur_dir):
        full_path = os.path.join(ab_dir_path,x)
        if os.path.isdir(full_path) and not x[0]=='.':

            print(os.stat(full_path),x)


simu_dir_l('../')


# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

def search(dir,str):
    list = [x for x in os.listdir(dir) if os.path.isfile(os.path.join(os.path.abspath(dir),x))]
    #fuck