#coding:utf-8
from selenium import webdriver
def zidian():
    dicts = {}
    f=open('F:\python\script\practice\canshuhua\login.txt','r')
    lines=f.readlines()
    print(lines)
    for line in lines:
        line = line.strip('\n')
        username = line.split(',')[0]
        password = line.split(',')[1]
        print(username, password)
        dicts[line.split(',')[0]] = line.split(',')[1]
    f.close()
    print(dicts)
    return(dicts)
