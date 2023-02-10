#coding:utf-8
from CustException.MyCusExcepion import FoundException

try:
    for row, record in enumerate(table):
        for col, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    raise FoundException()
except FoundException:
    print("Found at ({}, {1}, {2})".format(row, col, index))