#coding:utf-8
import os
import re
import logging


#定义一个函数，输入为接口类型，返回一段截取的同类型接口配置文本
def Interf_Cut(filepath, Inter_Type):
    f = open(filepath, 'r', encoding='utf-8')
    #将逐行读入的文件合并一个文本
    AllLines = ''.join(f.readlines())
    #根据接口硬件和虚拟类型分割文本，形成单独配置文本段落
    f.close()
    Inter_Re = re.compile(
        '''(?P<inter_Capall>(?P<Inter_T>\ninterface\s+''' + Inter_Type + ''').*?\n((?P<Null_Conf>.*(?P=Inter_T).*?\n.*?#\n)|(.*?#\n)))''',
        re.I | re.DOTALL)
    #查找到文本即返回文本段
    matchtest = Inter_Re.search(AllLines)
    if matchtest != None:
        Inter_Text = matchtest.groupdict()['inter_Capall']
        #rev13_Logger.debug(Inter_Text)
        return Inter_Text
    else:
        return None









