# TTLScan
**一款插件化的漏洞扫描器框架**


- 目前只支持ip iplist
- 目前支持RedisUn RedisGetShell Struts2系列漏洞 部分POC尚未检测有效性
- 后续添加Celery实现分布式调度
- 后续添加ZoomEYE搜索引擎
- To be Continued...

    
```

 20:20:08 | •100  tiaotiaolong  ttlscan 
❱ python ttlscan.py --iplist ip.txt --script redis_poc

▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄          ▄▄▄▄
▀▀▀██▀▀▀  ▀▀▀██▀▀▀  ██        ▄█▀▀▀▀█
   ██        ██     ██        ██▄        ▄█████▄   ▄█████▄  ██▄████▄
   ██        ██     ██         ▀████▄   ██▀    ▀   ▀ ▄▄▄██  ██▀   ██
   ██        ██     ██             ▀██  ██        ▄██▀▀▀██  ██    ██     author:跳跳龙
   ██        ██     ██▄▄▄▄▄▄  █▄▄▄▄▄█▀  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██     code by 2018-09-09
   ▀▀        ▀▀     ▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀

Wed, 12 Sep 2018 20:24:43  ttlscan.py   1536755083.07 scan starting
Wed, 12 Sep 2018 20:24:43  ttlscan.py   [+]Vuln: 127.0.0.1 has found Redis access without limit
Wed, 12 Sep 2018 20:24:43  ttlscan.py   [+]Vuln: 10.211.55.8 has found Redis access without limit

 20:24:43 | •100  tiaotiaolong  ttlscan 
❱ python ttlscan.py --ip 127.0.0.1  --script redis_poc

▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄          ▄▄▄▄
▀▀▀██▀▀▀  ▀▀▀██▀▀▀  ██        ▄█▀▀▀▀█
   ██        ██     ██        ██▄        ▄█████▄   ▄█████▄  ██▄████▄
   ██        ██     ██         ▀████▄   ██▀    ▀   ▀ ▄▄▄██  ██▀   ██
   ██        ██     ██             ▀██  ██        ▄██▀▀▀██  ██    ██     author:跳跳龙
   ██        ██     ██▄▄▄▄▄▄  █▄▄▄▄▄█▀  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██     code by 2018-09-09
   ▀▀        ▀▀     ▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀

Wed, 12 Sep 2018 20:24:57  ttlscan.py   1536755097.4 scan starting
Wed, 12 Sep 2018 20:24:57  ttlscan.py   [+]Vuln: 127.0.0.1 has found Redis access without limit
```


