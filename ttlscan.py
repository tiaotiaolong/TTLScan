#coding=utf-8
import argparse
from plugins import redis_poc
import logging
import time
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter
import importlib
import re
from lib import ttlscanlogger

#Logo
def print_logo():
	print '\033[0;31;40m'
	print "▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄          ▄▄▄▄"
	print "▀▀▀██▀▀▀  ▀▀▀██▀▀▀  ██        ▄█▀▀▀▀█"
	print "   ██        ██     ██        ██▄        ▄█████▄   ▄█████▄  ██▄████▄"
	print "   ██        ██     ██         ▀████▄   ██▀    ▀   ▀ ▄▄▄██  ██▀   ██"
	print "   ██        ██     ██             ▀██  ██        ▄██▀▀▀██  ██    ██     author:跳跳龙"
	print "   ██        ██     ██▄▄▄▄▄▄  █▄▄▄▄▄█▀  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██     code by 2018-09-09"
	print "   ▀▀        ▀▀     ▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀"
	print '\033[0m'

#判断字符串是否为ip

def isIP(one_str):
    '''
    正则匹配方法
    判断一个字符串是否是合法IP地址
    '''
    compile_ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
    if compile_ip.match(one_str):  
        return True  
    else:  
        return False 


if __name__ == '__main__':
	#准备工作
	print_logo()
	time.sleep(1)
	ttlscanlogger.logger.info("{0} scan starting".format(time.time()))
	#parser
	parser=argparse.ArgumentParser(description="ttlscan help")
	parser.add_argument('--ip', type=str , help='ip to pentest')
	parser.add_argument('--iplist', type=str , help='file contained ips')
	parser.add_argument('--search', type=str, help='search engine to get ip')
	parser.add_argument('--script', type=str , help='script you want test')
	#参数传递
	args=parser.parse_args()
	ip,iplist,search,script=args.ip,args.iplist,args.search,args.script
	
	#逻辑判断
	#如果ip不为空 输入源为ip参数
	if not ip==None:
		#是合法ip
		if(isIP(ip)):
			module=importlib.import_module('plugins.{}'.format(script))
			if(module.POC(ip)):
				ttlscanlogger.logger.error("[+]Vuln: {0} has found Redis access without limit".format(ip))
	#ip为空 输入源有可能是iplist或者search
	else:
		#如果iplist不为空
		if not iplist==None:
			with open(iplist,'r') as f:
				ip_list=f.readlines()

			for ip in ip_list:
				ip=ip.strip()
				if(isIP(ip)):
					module=importlib.import_module('plugins.{}'.format(script))
					if(module.POC(ip)):
						ttlscanlogger.logger.error("[+]Vuln: {0} has found Redis access without limit".format(ip))
		else:
			#如果是搜索引擎输入源
			if not search==None:
				pass
			#输入源有误
			else:
				ttlscanlogger.logger.info("输入源有误 程序自动退出")
				exit(-1)
















