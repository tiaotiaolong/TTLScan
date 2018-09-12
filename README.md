# TTLScan
**一款插件化的漏洞扫描器框架**

目前只支持ip iplist 两种方式，后续会把利用搜索引擎进行爬取的功能实现，会陆续的编写POC，目前只支持Redis未授权访问。
    
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


