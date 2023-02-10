#coding:utf-8
from CustLogger.CustLog import Log as logger
import logging

glogger = logger(".\\CustLogger")
@glogger.log_wrapper("haha!")
def func(a, key="b"):
    return str(a ** 2) + " test"

print(func(2, key="myc"))

