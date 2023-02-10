#coding:utf-8

'''
  #测试文本是否在列表中，并找到某段文本的索引
'''


list = ['a', 'b, c, d', 'interface giga 1/0/0', 'port access vlan 20', 'description toshanghai']

if __name__ == '__main__':
    if "port access vlan" in str(list):
        print(True)