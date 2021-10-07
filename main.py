import configparser
import time
import start
import random

print(start.to_log("INFO", "程序启动。"))
conf = configparser.ConfigParser()
conf.read('./config.ini')

userdata = {
    "uid":"",
    "stoken":""
}
setting = {
    "module_id":"",
    "t1":"",
    "t2":"",
    "timeout":""
}

setting["module_id"] = conf.get("Settings", "module_id")
setting["t1"] = conf.get("Settings", "t1")
setting["t2"] = conf.get("Settings", "t2")
setting["timeout"] = conf.get("Settings", "timeout")

result_error = []
result_exception = []

def check(i):
    if conf.has_option("Cookies", "uid_{0}".format(i)) == False:
        return False
    elif conf.has_option("Cookies", "stoken_{0}".format(i)) == False:
        return False
    else:
        return True

i = 1
while True:
    userdata["uid"] = conf.get("Cookies", "uid_{0}".format(i))
    userdata["stoken"] = conf.get("Cookies", "stoken_{0}".format(i))
    result = start.start(userdata, setting)
    if result == "error":
        result_error.append(userdata["uid"])
    elif result != "success":
        result_exception.append(userdata["uid"])

    i += 1

    if check(i) == True:
        time.sleep(random.uniform(int(setting["t1"]), int(setting["t2"])))
    else:
        break

if result_error != []:
    it = iter(result_error)
    while True:
        try:
            print(start.to_log("WARN", "执行失败的用户：{0}".format(next(it))))
        except StopIteration:
            break
elif result_exception != []:
    it = iter(result_exception)
    while True:
        try:
            print(start.to_log("WARN", "执行异常的用户：{0}".format(next(it))))
        except StopIteration:
            break
else:
    print(start.to_log("INFO", "所有用户均操作完毕。"))

print(start.to_log("INFO", "程序结束。"))