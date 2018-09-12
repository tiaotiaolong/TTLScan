#coding=utf-8
import redis

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Redis未授权访问"
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

