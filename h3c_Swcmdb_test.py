#coding:utf-8

from CustException.H3cFindException import *
from H3cconfig_parser.h3c_switchCmdbv3 import H3cSw_Cmdb
from CustLogger.CustLog import Log
import logging
LogDir = "F:\\pythoncode\\Cmdb_Network_Analysis\\h3cCmdblog"
Glog = Log(log_dir=LogDir)
conf = "F:\\pythoncode\\Cmdb_Network_Analysis\\txtsource\配置信息\\核心.txt"
H3cCmdbTest = H3cSw_Cmdb(conf)
testdict = {}
conftext = '''
interface GigabitEthernet1/2/0/4
 port link-mode route
 description yidongzhuanxian
 ip address 10.10.210.2 255.255.255.252
 packet-filter 3333 inbound
 mirroring-group 6 mirroring-port both
#
interface GigabitEthernet2/2/0/4
 port link-mode route
 description CNC_to_hefei_service
 ip address 10.10.220.2 255.255.255.252
 packet-filter 3333 inbound
 mirroring-group 6 mirroring-port both
#
interface GigabitEthernet1/2/0/1
 port link-mode bridge
 description TO_EXT-FW-1
 port access vlan 80
 mirroring-group 5 mirroring-port both
#
interface GigabitEthernet1/2/0/2
 port link-mode bridge
 description TO-bangongServer-fw2
 port access vlan 50
 undo stp enable
#
interface GigabitEthernet1/2/0/3
 port link-mode bridge
#
interface GigabitEthernet1/2/0/5
 port link-mode bridge
#
interface GigabitEthernet1/2/0/6
 port link-mode bridge
 description mirroring_beijing_office_lan
 mirroring-group 1 monitor-port
#
interface GigabitEthernet1/2/0/7
 port link-mode bridge
 description mirroring_wuhu_office_lan
 mirroring-group 2 monitor-port
#
interface GigabitEthernet1/2/0/8
 port link-mode bridge
#
interface GigabitEthernet1/2/0/9
 port link-mode bridge
#
interface GigabitEthernet1/2/0/10
 port link-mode bridge
#
interface GigabitEthernet1/2/0/11
 port link-mode bridge
#
interface GigabitEthernet1/2/0/12
 port link-mode bridge
#
interface GigabitEthernet1/2/0/13
 port link-mode bridge
#
interface GigabitEthernet1/2/0/14
 port link-mode bridge
#              
interface GigabitEthernet1/2/0/15
 port link-mode bridge
 description mirroring_hefei_net
 mirroring-group 6 monitor-port
#
interface GigabitEthernet1/2/0/16
 port link-mode bridge
 description mirroring_ASP_10NET_lan
 mirroring-group 5 monitor-port
#
interface GigabitEthernet1/2/0/17
 port link-mode bridge
#
interface GigabitEthernet1/2/0/18
 port link-mode bridge
#
interface GigabitEthernet1/2/0/19
 port link-mode bridge
#              
interface GigabitEthernet1/2/0/20
 port link-mode bridge
#
interface GigabitEthernet1/2/0/21
 port link-mode bridge
#
interface GigabitEthernet1/2/0/22
 port link-mode bridge
#
interface GigabitEthernet1/2/0/23
 port link-mode bridge
#
interface GigabitEthernet1/2/0/24
 port link-mode bridge
#
interface GigabitEthernet2/2/0/1
 port link-mode bridge
 description TO_EXT-FW-2
 port access vlan 80
 mirroring-group 5 mirroring-port both
#
interface GigabitEthernet2/2/0/2
 port link-mode bridge
 description TO-bangongServer-fw2
 port access vlan 50
 undo stp enable
#
interface GigabitEthernet2/2/0/3
 port link-mode bridge
#
interface GigabitEthernet2/2/0/5
 port link-mode bridge
 description link_ZaibeiJuniper
 port access vlan 140
#
interface GigabitEthernet2/2/0/6
 port link-mode bridge
 description link_Test-FW
 port access vlan 56
 undo stp enable
#
interface GigabitEthernet2/2/0/7
 port link-mode bridge
 description mirroring_beijing_ser_lan
 mirroring-group 3 monitor-port
#
interface GigabitEthernet2/2/0/8
 port link-mode bridge
#
interface GigabitEthernet2/2/0/9
 port link-mode bridge
#
interface GigabitEthernet2/2/0/10
 port link-mode bridge
#
interface GigabitEthernet2/2/0/11
 port link-mode bridge
#
interface GigabitEthernet2/2/0/12
 port link-mode bridge
#
interface GigabitEthernet2/2/0/13
 port link-mode bridge
#
interface GigabitEthernet2/2/0/14
 port link-mode bridge
#
interface GigabitEthernet2/2/0/15
 port link-mode bridge
#
interface GigabitEthernet2/2/0/16
 port link-mode bridge
#
interface GigabitEthernet2/2/0/17
 port link-mode bridge
#              
interface GigabitEthernet2/2/0/18
 port link-mode bridge
#
interface GigabitEthernet2/2/0/19
 port link-mode bridge
#
interface GigabitEthernet2/2/0/20
 port link-mode bridge
#
interface GigabitEthernet2/2/0/21
 port link-mode bridge
#
interface GigabitEthernet2/2/0/22
 port link-mode bridge
#
interface GigabitEthernet2/2/0/23
 port link-mode bridge
 stp edged-port
#              
interface GigabitEthernet2/2/0/24
 port link-mode bridge
#
interface M-GigabitEthernet1/0/0/0
 description Management
 ip binding vpn-instance Management
 ip address 192.168.6.160 255.255.255.0
#
interface M-GigabitEthernet1/0/0/1
#
interface Ten-GigabitEthernet1/3/0/1
 port link-mode route
 description TO_ShengChanSW-1_10GE1/1/0/1
 mirroring-group 5 mirroring-port both
 qos apply policy 10net inbound 
 port link-aggregation group 101
#
interface Ten-GigabitEthernet1/3/0/2
 port link-mode route
 port link-aggregation group 1
#
interface Ten-GigabitEthernet1/3/0/3
 port link-mode route
 description link_BanGongHJ-SW1-G1/0/26
 packet-filter 3001 inbound
 mirroring-group 2 mirroring-port both
 port link-aggregation group 2
#
interface Ten-GigabitEthernet2/3/0/1
 port link-mode route
 mirroring-group 5 mirroring-port both
 qos apply policy 10net inbound 
 port link-aggregation group 101
#
interface Ten-GigabitEthernet2/3/0/2
 port link-mode route
 port link-aggregation group 1
#              
interface Ten-GigabitEthernet2/3/0/3
 port link-mode route
 description link_BanGongHJ-SW2-G2/0/26
 packet-filter 3001 inbound
 mirroring-group 2 mirroring-port both
 port link-aggregation group 2
#
interface Ten-GigabitEthernet1/2/0/25
 port link-mode bridge
#
interface Ten-GigabitEthernet1/2/0/26
 port link-mode bridge
#
interface Ten-GigabitEthernet1/2/0/27
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/4
 port link-mode bridge
#              
interface Ten-GigabitEthernet1/3/0/5
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/6
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/7
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/8
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/9
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/10
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/11
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/12
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/13
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/14
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/15
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/16
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/17
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/18
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/19
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/20
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/21
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/22
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/23
 port link-mode bridge
#              
interface Ten-GigabitEthernet1/3/0/24
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/25
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/26
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/27
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/28
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/29
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/30
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/31
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/32
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/33
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/34
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/35
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/36
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/37
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/38
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/39
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/40
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/41
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/42
 port link-mode bridge
#              
interface Ten-GigabitEthernet1/3/0/43
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/44
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/45
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/46
 port link-mode bridge
#
interface Ten-GigabitEthernet1/3/0/47
 port link-mode bridge
 description bfd-mad
 port access vlan 999
 undo stp enable
#
interface Ten-GigabitEthernet2/2/0/25
 port link-mode bridge
#
interface Ten-GigabitEthernet2/2/0/26
 port link-mode bridge
#
interface Ten-GigabitEthernet2/2/0/27
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/4
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/5
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/6
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/7
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/8
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/9
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/10
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/11
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/12
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/13
 port link-mode bridge
#              
interface Ten-GigabitEthernet2/3/0/14
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/15
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/16
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/17
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/18
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/19
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/20
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/21
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/22
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/23
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/24
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/25
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/26
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/27
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/28
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/29
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/30
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/31
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/32
 port link-mode bridge
#              
interface Ten-GigabitEthernet2/3/0/33
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/34
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/35
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/36
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/37
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/38
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/39
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/40
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/41
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/42
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/43
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/44
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/45
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/46
 port link-mode bridge
#
interface Ten-GigabitEthernet2/3/0/47
 port link-mode bridge
 description bfd-mad
 port access vlan 999
 undo stp enable
#
interface Ten-GigabitEthernet1/2/0/28
#
interface Ten-GigabitEthernet1/3/0/48
#
interface Ten-GigabitEthernet2/2/0/28
#
interface Ten-GigabitEthernet2/3/0/48

'''
interpattern = ['Giga', 'Ten-Giga']
Inter_Confit_Dict = {}
for ipattern in interpattern:
    interfacelist = H3cCmdbTest.Inter_FindAll(ipattern)
    for conftext in interfacelist:
        H3cCmdbTest.Inter_analy(ipattern, conftext)

Inter_Confit_Dict = H3cCmdbTest.getInterDict()

for k1, v1 in Inter_Confit_Dict.items():
    Glog.log_show_store("{0}:\n".format(k1), logging.DEBUG)
    for k2, v2 in v1.items():
        Glog.log_show_store("{0}:{1}".format(k2, v2),logging.DEBUG)


# for conf_section in list:
#     InterLevel = H3cCmdbTest.Inter_anaLevel(InterType, conf_section)
#     print(InterLevel)



