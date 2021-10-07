# 米游社每日任务工具
 **参照了 [@inky-s](https://github.com/inky-s) 的代码。** 

 **https://github.com/inky-s/myb_workflow** 

- 支持多用户批量操作
- 操作随机冷却时间
- 从配置文件中读取用户Cookies和程序设置
- 操作结果会写入日志文件
- 可以完成每日获取米游币和不同版区的经验任务

 **以下是使用方法：** 
1. 先设置好配置文件`config.ini`，包含：

    `uid`（米哈游通行证ID，与Cookies所需`stuid`是一样的）

    `stoken`（抓包获取，这个值似乎是不会变更的，不同设备上同一账号都一样）
    
    `module_id`(游戏板块ID，具体看`config.ini`里的注释）
    
    `t1` `t2`（操作冷却时间，具体看`config.ini`里的注释）

    `timeout`（服务器连接超时时间）

2. 运行`main.py`或运行[编译好的程序](https://github.com/FailDragon-Plus/auto_mys/releases)。

3. 可前往`./logs/mhytool.log`查看日志。



- Python新手，代码可能有点繁琐有点问题😂
- 
 **效果演示：**
 ```
2021-10-07 16:38:33  INFO  程序启动。  
2021-10-07 16:38:33  INFO  用户 888888888：开始任务。  
2021-10-07 16:38:35  ERROR  签到出错!  
2021-10-07 16:38:38  INFO  帖子ID：10510210 —— 阅读成功。  
... 
2021-10-07 16:38:46  ERROR  帖子ID：10510210 —— 点赞失败！  
...  
2021-10-07 16:39:04  INFO  帖子ID：10510177 —— 转发成功。  
2021-10-07 16:39:04  INFO  帖子相关操作结束。  
2021-10-07 16:39:04  INFO  用户 888888888：任务结束。  
2021-10-07 16:39:04  WARN  执行失败的用户：888888888  
2021-10-07 16:39:04  INFO  程序结束。    
2021-10-07 16:52:32  INFO  程序启动。  
2021-10-07 16:52:32  INFO  用户 279160783：开始任务。  
2021-10-07 16:52:34  WARN  签到失败或重复签到。  
2021-10-07 16:52:37  INFO  帖子ID：10510895 —— 阅读成功。  
...  
2021-10-07 16:52:48  INFO  帖子ID：10510895 —— 点赞成功。  
...  
2021-10-07 16:53:07  INFO  帖子ID：10510866 —— 转发成功。  
2021-10-07 16:53:07  INFO  帖子相关操作结束。  
2021-10-07 16:53:07  INFO  用户 279160783：任务结束。  
2021-10-07 16:53:07  INFO  所有用户均操作完毕。  
2021-10-07 16:53:07  INFO  程序结束。    
2021-10-07 17:01:28  INFO  程序启动。  
2021-10-07 17:01:28  INFO  用户 279160783：开始任务。  
2021-10-07 17:01:28  WARN  服务器连接失败。  
2021-10-07 17:01:28  WARN  服务器连接失败。  
2021-10-07 17:01:28  INFO  用户 279160783：任务结束。  
2021-10-07 17:01:28  WARN  执行失败的用户：279160783  
2021-10-07 17:01:28  INFO  程序结束。  
```
