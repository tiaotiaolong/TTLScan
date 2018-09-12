#coding=utf-8
import logging
import time
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter


#创建一个日志收集器logger
logger = logging.getLogger("autotest")

#修改日志的输出级别
logger.setLevel(logging.DEBUG)

#设置输出的日志内容格式
fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s   %(log_color)s%(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

formatter = ColoredFormatter(fmt=fmt,
                       datefmt=datefmt,
                       reset=True,
                       secondary_log_colors={},
                       style='%'
                       )

#设置输出渠道--输出到控制台
hd_1 = logging.StreamHandler()
#在handler上指定日志内容格式
hd_1.setFormatter(formatter)
# 将headler添加到日志logger上
logger.addHandler(hd_1)