import redis
import socket
from lib import ttlscanlogger

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Redis Access Without Limit"
	dict_poc["Chinese_name"]="Redis未授权访问"
	dict_poc["author"]="qi.tao"
	dict_poc["port"]=6379
	return dict_poc
	
def POC(ip,port=6379):
	try:
		socket.setdefaulttimeout(2)
		poc=b"\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a"
		s=socket.socket()
		s.connect((ip,port))
		s.send(poc)
		rec=s.recv(1024)
		s.close()
		if "redis" in rec.decode():
			ttlscanlogger.logger.error("[+]Vuln: {0} has found Redis access without limit".format(ip))
			return True
		else:
			return False
	except:
		return False

if __name__ == '__main__':
	print(POC())

