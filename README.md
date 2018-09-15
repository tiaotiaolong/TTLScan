# TTLScan
**一款插件化的漏洞扫描器框架**


- 目前只支持ip iplist
- 目前支持RedisUn RedisGetShell Struts2系列漏洞 
- POC的准确性的已被复测
- 后续添加ZoomEYE搜索引擎
- 后续添加Celery实现分布式调度
- To be Continued...

    
**截图**

![](http://okzjjcktf.bkt.clouddn.com/logo.png)

**使用说明**

程序的整体设计是支持3种输入源，目前支持两种输入源分别为：

- ip方式
- url方式

其中这两种都支持list形式 也就是文件列表格式。
eg: Redis未授权访问，输入源就是ip方式 你可以使用--ip或者--ip_list两种参数
其中--ip和--ip_list两者中--ip的优先级较高，如果同时使用了2种参数，则视为--ip_list无效

**Will Do**

- 将第三种输入源集成进来，对接Zoomeye。可以利用Zoomeye确定大量ip，并针对我们的Poc进行检测
- 当数量比较庞大的时候引入多线程以及协程相关技术
- 对扫描的数据进行存储
- Celery分布式任务处理






