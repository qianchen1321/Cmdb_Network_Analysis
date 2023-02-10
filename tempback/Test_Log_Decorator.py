"""
-*- coding:utf-8 -*-
@File: main.py
@Author:frank yu
@DateTime: 2021.10.12 20:56
@Contact: frankyu112058@gmail.com
@Description:
"""
from CustLogger.CustLog import Log, DEBUG, WARN, INFO
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


log = Log()


@log.log_wrapper("wrapper for test")
def test(a, b, c=5):
    log.log_show('main test 1 ' + str(a), level=DEBUG)
    log.log_show('main test 2 ' + str(b), level=WARN)
    log.log_store('main test 3 ' + str(a), level=DEBUG)
    log.log_store('main test 4 ' + str(b), level=WARN)
    log.log_show_store('main test 5 ' + str(a + b), level=INFO)
    return a + b + c


def even(num):
    log.log_store('main even 1 ' + str(num), level=INFO)


def odd(num):
    log.log_store('main odd 1 ' + str(num), level=INFO)


# multi thread test
def multi_thread():
    exe = ThreadPoolExecutor(4)
    for i in range(10):
        if i & 1 == 0:
            exe.submit(even, i)
        else:
            exe.submit(odd, i)


# multi process test
def multi_process():
    exe = ProcessPoolExecutor(4)
    for i in range(10):
        if i & 1 == 0:
            exe.submit(even, i)
        else:
            exe.submit(odd, i)


if __name__ == '__main__':
    test(3, 4, 6)
    multi_thread()
    multi_process()