#coding:utf-8
#华三交换机分析类
import re
from CustException.H3cFindException import *

class H3cSw_Cmdb:
    #2层模型配置相关正则

    RE_DESC = re.compile("(description.*?\n)", re.I | re.DOTALL | re.MULTILINE)
    RE_PORTVLAN = re.compile("(port access vlan\s+.*?\n)", re.I | re.DOTALL | re.MULTILINE)
    RE_MirrorGroup = re.compile("mirroring-group (\d).*?\n", re.I | re.DOTALL | re.MULTILINE)
    RE_Aggreg = re.compile("port link-aggregation group (\d+)", re.I | re.DOTALL | re.MULTILINE)
    #华三交换机固定三层接口类别
    INTERL3TYPE = ['NULL', 'LOOPBack', 'Vlan', 'Route-Aggregation', 'M-Giga']
    #华三交换机固定二层三层同时支持接口类别，需要根据命令解析去判断
    INTERl2L3TYPE = ['Giga',  'Ten-Giga']
    #初始化switch cmdb解析类
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
            self.Sw_Inter_Dict = {}
            for intertype1 in self.INTERl2L3TYPE:
                self.Sw_Inter_Dict[intertype1] = {}
            for intertype2 in self.INTERL3TYPE:
                self.Sw_Inter_Dict[intertype2] = {}



    def getInterDict(self):
        return self.Sw_Inter_Dict
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

    #根据接口类型名称，切出相关接口的配置文本列表
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


    #纯2层接口文本分析，将接口配置返回一个该接口的一个字典
    def __H3l2inter_analy__(self, Dict={}, conftext=" "):
        if "undo stp enable" in conftext:
            Dict['stp'] = "disabled"
        else:
            Dict['stp'] = "enabled"
        #获取接口vlan号
        match = self.RE_PORTVLAN.search(conftext)
        if match:
            Dict["vlan"] = match.group(0).split("vlan")[1].strip()
        else:
            Dict["vlan"] = 1

        #镜像源端口配置
        match = self.RE_MirrorGroup.search(conftext)
        if match:
            Dict["mirrorGroupSource"] = match.group(1)
        else:
            Dict["mirrorGroupSource"] = 0

        #端口聚合配置检查
        match = self.RE_Aggreg.search(conftext)
        if match:
            Dict['Aggroup'] = match.group(1)
        else:
            Dict['Aggroup'] = 0


    def __H3l3inter_analy__(self, Dict, conftext):
        pass

    def Inter_analy(self, intertype, conftxt):
        #文本切分成列表
        conflist = conftxt.strip().split("\n")
        '''将列表尾部的#号标志位去除'''
        #conflist.pop()
        #通过列表获取本文本中的接口完整名称
        ThisInter = re.split(r'\s+',conflist[0])[1]
        thisInter_Dict = {}
       #构建一个本接口名的完整配置字段
        nesInterDict = {}


        if intertype in H3cSw_Cmdb.INTERl2L3TYPE:

            # 设置嵌套字典中的接口配置，以接口名称为键
            self.Sw_Inter_Dict[intertype][ThisInter] = thisInter_Dict

            #首先获取接口描述
            match = self.RE_DESC.search(conftxt)
            if match:
                thisInter_Dict['Description'] = match.group().split(" ")[1].strip()
            else:
                thisInter_Dict['Description'] = "未配置描述"
            #判断是否为镜像目标端口
            MatchMonitor = re.search(r'mirroring-group (\d) monitor-port', conftxt)
            if MatchMonitor:
                thisInter_Dict['type'] = 'Span Monitor'
                thisInter_Dict['Monitor_Group'] = MatchMonitor.group(1)
                return  '镜像目标口'
            #判断端口是否二层端口模式
            if "port link-mode bridge" in conftxt:
                thisInter_Dict['type'] = 'L2'
                self.__H3l2inter_analy__(thisInter_Dict, conftxt)
                return 'l2 interface'
            else:
                 thisInter_Dict['type'] = 'L3'
                 self.__H3l3inter_analy__(thisInter_Dict, conftxt)
                 return "l3 interface"



