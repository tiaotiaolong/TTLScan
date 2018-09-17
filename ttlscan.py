#coding=utf-8
import argparse
import logging
import time
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter
import importlib
import re
from lib import ttlscanlogger
import os
from os import path
#Logo
def print_logo():
	print('\033[0;31;40m')
	print("▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄          ▄▄▄▄")
	print("▀▀▀██▀▀▀  ▀▀▀██▀▀▀  ██        ▄█▀▀▀▀█")
	print("   ██        ██     ██        ██▄        ▄█████▄   ▄█████▄  ██▄████▄")
	print("   ██        ██     ██         ▀████▄   ██▀    ▀   ▀ ▄▄▄██  ██▀   ██")
	print("   ██        ██     ██             ▀██  ██        ▄██▀▀▀██  ██    ██     author:跳跳龙")
	print("   ██        ██     ██▄▄▄▄▄▄  █▄▄▄▄▄█▀  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██     scripts: 9")
	print("   ▀▀        ▀▀     ▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀     code by 2018-09-09")
	print('\033[0m')


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

def scan_over(start_time):
	over_time=time.time()
	ttlscanlogger.logger.info("程序本次用时 {}s".format(over_time-start_time))
	exit(0)

def scan_over_error():
	ttlscanlogger.logger.info("输入源有误 程序自动退出")
	exit(-1)



if __name__ == '__main__':
	#准备工作
	print_logo()
	start_time=time.time()
	#parser
	parser=argparse.ArgumentParser(description="ttlscan help")
	parser.add_argument('--ip', type=str , help='ip to pentest')
	parser.add_argument('--ip_list', type=str , help='file contained ips')
	parser.add_argument('--target_url',type=str, help="target url")
	parser.add_argument('--target_url_list',type=str, help="target url list")
	parser.add_argument('--search', type=str, help='search engine to get ip')
	parser.add_argument('--script', type=str , help='script you want test')
	parser.add_argument('--query', type=str , help='eg: python ttlscan.py --query scripts')
	#参数传递
	args=parser.parse_args()
	ip,ip_list,search,target_url,target_url_list,script=args.ip,args.ip_list,args.search,args.target_url,args.target_url_list,args.script
	query=args.query

	#逻辑判断
	#查询功能
	if query=="scripts":
		scripts_url_list=os.listdir(os.path.dirname(os.path.realpath(__file__))+"/plugins/url")
		scripts_ip_list=os.listdir(os.path.dirname(os.path.realpath(__file__))+"/plugins/ip")
		scripts_list=scripts_url_list+scripts_ip_list
		temp=[]
		for script in scripts_list:
			if re.search('.py$',script) and 'init' not in script:
				temp.append(script.split('.')[0])
		ttlscanlogger.logger.info("scripts: {0}".format('    '.join(temp)))
		scan_over(start_time)
		
	ttlscanlogger.logger.info("{0} scan starting".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) ))
	#基于IP
	if not ip==None:
		#是合法ip
		if(isIP(ip)):
			#动态调用
			module=importlib.import_module('plugins.ip.{}'.format(script))
			module.POC(ip)
			#Over
			scan_over(start_time)
			
	#基于IPLIST
	if not ip_list==None:
		with open(ip_list,'r') as f:
				ip_list_temp=f.readlines()

		for ip in ip_list_temp:
			ip=ip.strip()
			if(isIP(ip)):
				module=importlib.import_module('plugins.ip.{}'.format(script))
				module.POC(ip)
		scan_over(start_time)

	#基于第三方搜索引擎
	if not search==None:
		pass
		exit(0)

	#基于URL
	if not target_url==None:
		module=importlib.import_module('plugins.url.{}'.format(script))
		module.POC(target_url)
		scan_over(start_time)

	#基于URLLIST
	if not target_url_list==None:
		with open(target_url_list,'r') as f:
				url_list_temp=f.readlines()
		for url in url_list_temp:
			url=url.strip()
			module=importlib.import_module('plugins.url.{}'.format(script))
			module.POC(target_url)
		scan_over(start_time)

	#输入源有误
	else:
		scan_over_error()
		
















