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

2. 运行`main.py`。

3. 可前往`./logs/mhytool.log`查看日志。


- Python新手，代码可能有点繁琐有点问题😂
