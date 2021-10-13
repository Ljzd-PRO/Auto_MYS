import configparser
import time
import start
import random
import sys
import os

def get_file_path(file_name=""):
    """
    获取文件绝对路径, 防止在某些情况下报错
    :param file_name: 文件名
    :return:
    """
    return os.path.join(os.path.split(sys.argv[0])[0], file_name)

print(start.to_log("INFO", "程序启动。"))
conf = configparser.ConfigParser()
conf.read(get_file_path("config.ini"))

userdata = {
    "uid":"",
    "stoken":"",
    "id":""
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

timesleep_1 = setting["t1"]
timesleep_2 = setting["t2"]
if timesleep_1 == '' or None:
    timesleep_1 = 2
if timesleep_2 == '' or None:
    timesleep_2 = 4
timesleep_1 = int(timesleep_1)
timesleep_2 = int(timesleep_2)

result_error = {}
result_exception = {}

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
    userdata["id"] = str(i)
    result = start.start(userdata, setting)
    if result == "error":
        result_error[str(i)] = userdata["uid"]
    elif result != "success":
        result_exception[str(i)] = userdata["uid"]

    i += 1
    if check(i) == True:
        time.sleep(random.uniform(timesleep_1, timesleep_2))
    else:
        break

## 检查是否有执行失败的用户
if result_error == {}:
    if result_exception == {}:
        print(start.to_log("INFO", "所有用户均操作完毕。"))
        print(start.to_log("INFO", "程序结束。"))
        exit(0)
if result_error != {}:
    it = iter(result_error)
    while True:
        try:
            error_id = next(it)
            print(start.to_log("WARN", "执行失败的用户：uid_{0} - {1}".format(error_id, result_error[error_id])))
        except StopIteration:
            break
if result_exception != {}:
    it = iter(result_exception)
    while True:
        try:
            exception_id = next(it)
            print(start.to_log("WARN", "执行异常的用户：uid_{0} - {1}".format(exception_id, result_exception[exception_id])))
        except StopIteration:
            break

## 重试执行失败和异常的用户任务
print(start.to_log("INFO", "正在重启执行失败和异常用户的任务。"))
if result_error != {}:
    it = iter(result_error)
    while True:
        try:
            error_id = next(it)
            userdata["uid"] = conf.get("Cookies", "uid_{0}".format(error_id))
            userdata["stoken"] = conf.get("Cookies", "stoken_{0}".format(error_id))
            userdata["id"] = error_id
            result = start.start(userdata, setting)
            if result == "success":
                del result_error[error_id]
        except StopIteration:
            break
if result_exception != {}:
    it = iter(result_exception)
    while True:
        try:
            exception_id = next(it)
            userdata["uid"] = conf.get("Cookies", "uid_{0}".format(exception_id))
            userdata["stoken"] = conf.get("Cookies", "stoken_{0}".format(exception_id))
            result = start.start(userdata, setting)
            if result == "success":
                del result_exception[exception_id]
        except StopIteration:
            break

## 再次检查执行失败的用户
if result_error == {}:
    if result_exception == {}:
        print(start.to_log("INFO", "所有用户均操作完毕。"))
        print(start.to_log("INFO", "程序结束。"))
        exit(0)
if result_error != {}:
    it = iter(result_error)
    while True:
        try:
            error_id = next(it)
            print(start.to_log("WARN", "依旧执行失败的用户：uid_{0} - {1}".format(error_id, result_error[error_id])))
        except StopIteration:
            break
if result_exception != {}:
    it = iter(result_exception)
    while True:
        try:
            exception_id = next(it)
            print(start.to_log("WARN", "依旧执行异常的用户：uid_{0} - {1}".format(exception_id, result_exception[exception_id])))
        except StopIteration:
            break
print(start.to_log("INFO", "程序结束。"))
