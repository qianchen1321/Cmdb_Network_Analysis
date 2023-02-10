#coding:utf-8
#华三交换机分析类
import re
from CustException.H3cFindException import *
class H3cSw_Cmdb:

    #华三交换机固定三层接口类别
    INTERL3TYPE = ['NULL', 'LOOPBack', 'Vlan', 'Route-Aggregation', 'M-Giga']
    #华三交换机固定二层三层同时支持接口类别，需要根据命令解析去判断
    INTERl2L3TYPE = ['Giga',  'Ten-Giga',]

    def __init__(self, ConfFile):

        try:
            self.confile = ConfFile

        except IOError as err:
            print(err)
        finally:
            # 根据接口硬件和虚拟类型分割文本，形成单独配置文本段落
            self.f = open(self.confile, 'r', encoding='utf-8')
            # 将逐行读入的文件合并一个文本
            self.AllLines = ''.join(self.f.readlines())
            self.f.close()


    # 定义一个函数，输入为接口类型，返回一段截取的同类型接口配置文本
    def Interf_Cut(self, Interpattern="giga"):

        Inter_Re = re.compile(
            '''(?P<inter_Capall>(?P<Inter_T>\ninterface\s+''' + Interpattern + ''').*?\n((?P<Null_Conf>.*(?P=Inter_T).*?\n.*?#\n)|(.*?#\n)))''',
            re.I | re.DOTALL)
        # 查找到文本即返回文本段
        match = Inter_Re.search(self.AllLines)
        if match != None:
            Inter_Text = match.groupdict()['inter_Capall']
            # rev13_Logger.debug(Inter_Text)
            return Inter_Text
        else:
            raise H3cInterCutExcep("无法截取接口类型相关的整段文本，可能是接口类型错误")

    def Inter_FindAll(self, Interpattern="Giga"):
        Inter_Re = re.compile(
            '''(?P<Interconf>^interface\s+''' + Interpattern + '''.*?#)''',
            re.I | re.DOTALL |re.MULTILINE)
        # 返回所有获取的列表
        InterconfList = Inter_Re.findall(self.AllLines)

        if not InterconfList:
            raise H3cInterFindExcep("无法获取接口列表，请确认接口类型是否正确")
        else:
            return InterconfList

    def Inter_analy(self, intertype, conftxt):
        #将接口文本逐行拆分成列表
        confinterlist = conftxt.strip().split("\n")
        #去除列表尾部#号
        confinterlist.pop()
        #获取接口名称
        ThisInter = confinterlist[0].split(" ")[1]
        confDict = {}
        confDict["intername"] = ThisInter

        if intertype in H3cSw_Cmdb.INTERl2L3TYPE:
            if "port link-mode bridge" in conftxt:
                print(" ".join([ThisInter, "本接口配置为2层模式"]))
                if len(confinterlist) <= 2:
                    print(" ".join([ThisInter, "为默认两层配置"]))
                    confDict["mode"] = "access port"
                    confDict["vlan"] = 1
                    return confDict




            elif "port link-aggregation group" in conftxt:
                print(ThisInter + "本接口配置为3层模式下的端口捆绑模式")
            else:
                print(ThisInter + "本接口配置为存粹三层模式")

    def H3cl2inter_analy(conftext):
        pass

    def H3cl2inter_analy(conftext):
        pass
