# dtutils
## 前提
python中常用的日期时间转换工具有datetime和time，用法很详细复杂，复杂到每次使用的时候必须对照着文档使用。
特别是在获取当前日期时间，日前时间转换成时间戳，时间戳转换成日期时间，时间差等时，要对照文档，使用比较麻烦。
本项目旨在进一步有需要的封装datetime和time，以简化使用。如有别的常用函数需要，欢迎提出。

## 提供的函数有
def nowdatetime(type="%Y-%m-%d %H:%M:%S")<br>
获取当前日期时间<br>
:param type: 输出的日期时间格式，默认是"%Y-%m-%d %H:%M:%S",要显示毫秒"%Y-%m-%d %H:%M:%S.%f"<br>
:return: 日期时间str<br><br>
def nowdate(type="%Y-%m-%d")<br>
获取当前日期<br>
:param type: 输出的日期格式，默认是"%Y-%m-%d"<br>
:return: 日期str<br><br>
def nowtime(type="%H:%M:%S")<br>
获取当前时间<br>
    :param type: 输出的时间格式，默认是"%H:%M:%S",要显示毫秒"%H:%M:%S.%f"<br>
    :return: 时间str<br>
def nowtimetag()<br>
获取当前日期时间对应的时间戳（秒级）<br>
    :return: 秒级时间戳int<br><br>
def nowmillitimetag()<br>
获取当前日期时间对应的时间戳（毫秒级）<br>
    :return:毫秒级时间戳int<br><br>
def timetag2datetime(timetag, type="%Y-%m-%d %H:%M:%S")<br>
时间戳转换成日期时间<br>
    :param timetag:时间戳，int，float，秒级或毫秒级时间戳都行<br>
    :param type:转换的日期时间格式，默认"%Y-%m-%d %H:%M:%S"<br>
    :return:指定格式的日期时间str<br><br>
def datetime2timetag(strdatetime,type="%Y-%m-%d %H:%M:%S")<br>
日期时间转换成秒级时间戳<br>
    :param strdatetime: str，日期时间<br>
    :param type: str，传入的日期时间的格式,默认是"%Y-%m-%d %H:%M:%S"<br>
    :return: int，时间戳<br><br>
def datetime2millitimetag(strdatetime,type="%Y-%m-%d %H:%M:%S.%f")<br>
日期时间转换成毫秒级时间戳<br>
    :param strdatetime: str，日期时间<br>
    :param type: str，传入的日期时间的格式，默认是"%Y-%m-%d %H:%M:%S.%f"<br>
    :return: int，时间戳<br><br>
def deltadatetime(strdatetime=None, days=0, hours=0, minutes=0, seconds=0, milliseconds=0,type="%Y-%m-%d %H:%M:%S")<br>
获取某个时间间隔后的日期时间<br>
    :param strdatetime: 参照日期时间，如果不填则使用当前日期时间<br>
    :param days:间隔的天数，默认0<br>
    :param hours:间隔小时数，默认0<br>
    :param minutes:间隔的分钟数，默认0<br>
    :param seconds:间隔的秒数，默认0<br>
    :param milliseconds:间隔的毫秒数，默认0<br>
    :param type:参照日期时间格式和输出的日期时间格式<br>
    :return:str<br>

## 安装使用
pip install dtutils

## 使用示例 
```python
from dtutils import *

if __name__=="__main__":
    print(nowdatetime('%Y-%m-%d %H:%M:%S.%f'))#当前日期时间，精确到毫秒
    print(nowdate())#当前日期
    print(nowtime())#当前时间
    print(nowtimetag())#当前秒级时间戳
    print(nowmillitimetag())#当前毫秒级时间戳
    print(timetag2datetime(nowmillitimetag()))#时间戳转成日期时间
    time.sleep(5)
    print(timetag2datetime(nowtimetag()))#时间戳转成日期时间
    nowstr = timetag2datetime(nowmillitimetag(), '%Y%m%d %H%M%S.%f')
    print(nowstr)
    print(datetime2timetag(nowstr,type='%Y%m%d %H%M%S.%f'))#日期时间转成秒级时间戳
    print(datetime2millitimetag(nowstr, type='%Y%m%d %H%M%S.%f'))#日期时间转成毫秒级时间戳
    print(deltadatetime(nowstr,hours=-10,seconds=-150,type='%Y%m%d %H%M%S.%f'))#相差某个时间后的日期时间
```
