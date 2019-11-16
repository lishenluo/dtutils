# dtutils
## 前提
python中常用的日期时间转换工具有datetime和time，用法很详细复杂，复杂到每次使用的时候必须对照着文档使用。
特别是在获取当前日期时间，日前时间转换成时间戳，时间戳转换成日期时间，时间差等时，要对照文档，使用比较麻烦。
本项目旨在进一步有需要的封装datetime和time，以简化使用。如有别的常用函数需要，欢迎提出。

## 提供的函数有
nowdatetime:获取当前日期时间<br>
nowdate:获取当前日期<br>
nowtime:获取当前时间<br>
nowtimetag:获取当前日期时间对应的时间戳（秒级）<br>
nowmillitimetag:获取当前日期时间对应的时间戳（毫秒级）<br>
timetag2datetime:时间戳转换成日期时间<br>
datetime2timetag:日期时间转换成秒级时间戳<br>
datetime2millitimetag:日期时间转换成毫秒级时间戳<br>
deltadatetime:获取某个时间间隔后的日期时间<br>

## 下载使用
下载整个文件夹dtutils,把该文件夹存放在python的安装目录下存放第三方库的Lib下的site-packages文件夹下。

## 使用示例 
```python
from DTUtils import *

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
