import json

#解析zoomeye的数据 获取目标ip
def parser(zoomeye_data):
	list=[]
	zoomeye_json=json.loads(zoomeye_data)
	for item in zoomeye_json['matches']:
		list.append(item['ip'])
	return list

