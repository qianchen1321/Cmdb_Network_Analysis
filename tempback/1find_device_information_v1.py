#!/usr/bin/python
# coding=utf-8
import logging

# 读取设备配置文件，以F5举例，读取F5的vs的名称和IP信息，截取字段关键信息，"ltm virtual"和"destination"

import os
import time

def get_device_information(inputfile,outputfile1,outputfile2):
    with open(inputfile, 'r') as f:
        lines = f.readlines()  # 读取后以行进行分隔
        for line in lines:
            try:
                if "ltm virtual /Common/" in line:  # 判断每行里面是否有关键信息
                    # 以‘/’为分隔符号，取分隔后的第3个元素，然后在以' '分隔，取分隔后的第0个元素
                    vs_name = line.split('/')[2].split(' ')[0]
                    print (vs_name)
                    with open(outputfile1, 'a') as f1:
                        f1.write(vs_name + '\n')
            except Exception as e:
                print(e)
            try:
                if "destination /Common/" in line:
                    dest_ip = line.split('/')[2]
                    print (dest_ip)
                    with open(outputfile2, 'a') as f2:
                        f2.write(dest_ip)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    starttime = time.time()  # 开始时间
    inputfile='f5_1.cfg'
    outputfile1='vs_name.txt'
    outputfile2='vs_address.txt'
    if os.path.exists(outputfile1):
        os.remove(outputfile1)
    if os.path.exists(outputfile2):
        os.remove(outputfile2)
    get_device_information(inputfile,outputfile1,outputfile2)
    endtime=time.time()
    print ('完成'+'花费时间:'+str(endtime-starttime))

