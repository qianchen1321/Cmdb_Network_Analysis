#coding:utf-8

from checktags.checktags import parse
import sys

if len(sys.argv) < 2:
    print("Usage: checktags,py infile1 [infile2 [...fileN]]")
    sys.exit

for filename in sys.argv[1:]:
    parse(filename)