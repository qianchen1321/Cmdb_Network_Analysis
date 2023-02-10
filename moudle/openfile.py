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


if __name__ == '__main__':
    # 定义一个函数，输入为接口类型，返回一段截取的同类型接口配置文本
    rev13_Logger = logging.getLogger("rev13back_Logger")
    filepath = 'log_rev13.log'
    if os.path.exists(filepath):
        os.remove(filepath)
    file_Rev13handler = logging.FileHandler(filepath, encoding='utf-8')
    filefmt = "%(name)-15s [%(filename)s %(lineno)d] %(message)s"
    fileformat = logging.Formatter(filefmt)
    file_Rev13handler.setFormatter(fileformat)
    rev13_Logger.addHandler(file_Rev13handler)
    console_Handler = logging.StreamHandler()
    console_fmt = "%(name)-15s [%(filename)s %(lineno)d] %(message)s"
    console_Formater = logging.Formatter(console_fmt)
    console_Handler.setFormatter(console_Formater)
    rev13_Logger.addHandler(console_Handler)
    rev13_Logger.setLevel(logging.DEBUG)

    Filepath = '..\\txtsource\\配置信息\\核心.txt'
    InterTypes = ['Giga', 'M-Giga', 'Ten-Giga', 'NULL', 'LOOPBack', 'Vlan', 'Route-Aggregation']
    Inter_Type = 'Route-Aggregation'
    InterSplit_Txt = Interf_Cut(Filepath, Inter_Type)
    if InterSplit_Txt != None:
        rev13_Logger.debug(InterSplit_Txt)
    else:
        rev13_Logger.debug("接口类型可能存在错误，截取配置端出错")







