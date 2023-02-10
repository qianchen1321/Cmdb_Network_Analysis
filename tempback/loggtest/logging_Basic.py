#coding:utf-8
import logging

#创建日志对象
logger = logging.getLogger("myTestLog")

#设置logger可输出日志级别范围
logger.setLevel(logging.DEBUG)
#添加控制台handler
console_Handler = logging.StreamHandler()
#添加文件handler
filehandler = logging.FileHandler(filename="testlog1.log", encoding='utf-8')

#添加handler 到日志器中
logger.addHandler(console_Handler)
logger.addHandler(filehandler)

#设置格式并赋于 handler
fromtter = logging.Formatter('%(asctime)s-%(name)s - %(levelname)s - %(message)s')
console_Handler.setFormatter(fromtter)
filehandler.setFormatter(fromtter)

logger.debug("====[开始测试]======")
logger.info("====[开始测试]======")
logger.warning("====[开始测试]======")
logger.critical("====[开始测试]======")
logger.error("====[开始测试]======")
