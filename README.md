# TTLScan
**一款插件化的漏洞扫描器框架**


- 目前只支持ip iplist
- 目前支持RedisUn RedisGetShell Struts2系列漏洞 
- 后续添加Celery实现分布式调度
- 后续添加ZoomEYE搜索引擎
- To be Continued...

    
```

 20:20:08 | •100  tiaotiaolong  ttlscan 
❱ python ttlscan.py --iplist ip.txt --script redis_un

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
❱ python ttlscan.py --ip 127.0.0.1  --script redis_un

▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄          ▄▄▄▄
▀▀▀██▀▀▀  ▀▀▀██▀▀▀  ██        ▄█▀▀▀▀█
   ██        ██     ██        ██▄        ▄█████▄   ▄█████▄  ██▄████▄
   ██        ██     ██         ▀████▄   ██▀    ▀   ▀ ▄▄▄██  ██▀   ██
   ██        ██     ██             ▀██  ██        ▄██▀▀▀██  ██    ██     author:跳跳龙
   ██        ██     ██▄▄▄▄▄▄  █▄▄▄▄▄█▀  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██     code by 2018-09-09
   ▀▀        ▀▀     ▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀

Wed, 12 Sep 2018 20:24:57  ttlscan.py   1536755097.4 scan starting
Wed, 12 Sep 2018 20:24:57  ttlscan.py   [+]Vuln: 127.0.0.1 has found Redis access without limit

 18:10:23 | •100  tiaotiaolong  TTLScan  G:  master   ⭑ - ? 
❱ python ttlscan.py --target_url http://127.0.0.1/memocreate.action  --script struts2_032

▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄  ▄▄          ▄▄▄▄
▀▀▀██▀▀▀  ▀▀▀██▀▀▀  ██        ▄█▀▀▀▀█
   ██        ██     ██        ██▄        ▄█████▄   ▄█████▄  ██▄████▄
   ██        ██     ██         ▀████▄   ██▀    ▀   ▀ ▄▄▄██  ██▀   ██
   ██        ██     ██             ▀██  ██        ▄██▀▀▀██  ██    ██     author:跳跳龙
   ██        ██     ██▄▄▄▄▄▄  █▄▄▄▄▄█▀  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██     scripts: 9
   ▀▀        ▀▀     ▀▀▀▀▀▀▀▀   ▀▀▀▀▀      ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀     code by 2018-09-09

Sat, 15 Sep 2018 18:12:43  ttlscan.py   Sat Sep 15 18:12:43 2018 scan starting
Sat, 15 Sep 2018 18:12:44  struts2_032.py   [+]Vuln: http://127.0.0.1/memocreate.action has found Struts2_032 vulnerabillity
Sat, 15 Sep 2018 18:12:44  ttlscan.py   scan over during 0.632119894028s
```


