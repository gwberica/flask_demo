import time


def unix_time(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp