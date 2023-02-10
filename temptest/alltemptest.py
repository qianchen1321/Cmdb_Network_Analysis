#coding:utf-8
text1 = '''
interface GigabitEthernet2/2/0/7
     port link-mode bridge
     description mirroring_beijing_ser_lan
     mirroring-group 3 monitor-port
#
'''

text2 = '''
interface Ten-GigabitEthernet1/3/0/1
 port link-mode route
 description TO_ShengChanSW-1_10GE1/1/0/1
 mirroring-group 5 mirroring-port both
 qos apply policy 10net inbound 
 port link-aggregation group 101
#
'''

# import re
# RE_MirrorGroup = re.compile("mirroring-group (\d).*?\n", re.I | re.DOTALL | re.MULTILINE)
# #match = re.search(r'mirroring-group (\d) mirroring-port.*?\n', text1)
# match = RE_MirrorGroup.search(text2)
# print(match.group(1))

def testdictadd(dict={}):
    dict['b'] = 2
    dict['c'] = 3
dict1 = {'a': 1}
testdictadd(dict1)


