#coding:utf-8
import re
import os
import logging

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

#logging.disable(logging.DEBUG)
from pprint import pprint

with open('../../txtsource/配置信息/核心.txt', 'r', encoding='utf-8') as f:
    AllLines = ''.join(f.readlines())
    #pprint(AllLines)
    #rev13_Logger.debug(AllLines)
    Inter_Type = "Giga"
    Inter_Re = re.compile('''(?P<inter_Capall>(?P<Inter_T>interface\s+''' + Inter_Type + ''').*?\n.*(?P=Inter_T).*?\n#\n)''', re.I|re.DOTALL)
    matchtest = Inter_Re.search(AllLines)
    Inter_Text = matchtest.groupdict()['inter_Capall']
    rev13_Logger.debug(Inter_Text)



