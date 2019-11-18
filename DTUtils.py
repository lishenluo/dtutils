#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 15:01
# @Author  : lishenluo
# @Email   : lishenluo@163.com
import datetime,time

def nowdatetime(type="%Y-%m-%d %H:%M:%S"):
    '''
    获取当前日期时间
    :param type: 输出的日期时间格式，默认是"%Y-%m-%d %H:%M:%S",要显示毫秒"%Y-%m-%d %H:%M:%S.%f"
    :return: 日期时间str
    '''
    return datetime.datetime.now().strftime(type)

def nowdate(type="%Y-%m-%d"):
    '''
    获取当前日期
    :param type: 输出的日期格式，默认是"%Y-%m-%d"
    :return: 日期str
    '''
    return datetime.datetime.now().strftime(type)

def nowtime(type="%H:%M:%S"):
    '''
    获取当前时间
    :param type: 输出的时间格式，默认是"%H:%M:%S",要显示毫秒"%H:%M:%S.%f"
    :return: 时间str
    '''
    return datetime.datetime.now().strftime(type)

def nowtimetag():
    '''
    获取当前日期时间对应的时间戳（秒级）
    :return: 秒级时间戳int
    '''
    return int(time.time())

def nowmillitimetag():
    '''
    获取当前日期时间对应的时间戳（毫秒级）
    :return:毫秒级时间戳int
    '''
    return int(round(time.time()*1000))

def timetag2datetime(timetag, type="%Y-%m-%d %H:%M:%S"):
    '''
    时间戳转换成日期时间
    :param timetag:时间戳，int，float，秒级或毫秒级时间戳都行
    :param type:转换的日期时间格式，默认"%Y-%m-%d %H:%M:%S"
    :return:指定格式的日期时间str
    '''
    #传入的是毫秒级的时间戳
    if timetag > 10 ** 10:
        timetag = timetag/1000.0
    datetime_array = datetime.datetime.fromtimestamp(timetag)
    return datetime_array.strftime(type)

def datetime2timetag(strdatetime,type="%Y-%m-%d %H:%M:%S"):
    '''
    日期时间转换成秒级时间戳
    :param strdatetime: str，日期时间
    :param type: str，传入的日期时间的格式,默认是"%Y-%m-%d %H:%M:%S"
    :return: int，时间戳
    '''
    datetime_mid = datetime.datetime.strptime(strdatetime, type)
    return  int(time.mktime(datetime_mid.timetuple()))

def datetime2millitimetag(strdatetime,type="%Y-%m-%d %H:%M:%S.%f"):
    '''
    日期时间转换成毫秒级时间戳
    :param strdatetime: str，日期时间
    :param type: str，传入的日期时间的格式，默认是"%Y-%m-%d %H:%M:%S.%f"
    :return: int，时间戳
    '''
    datetime_mid = datetime.datetime.strptime(strdatetime, type)
    return  int(time.mktime(datetime_mid.timetuple()))*1000+int(round(datetime_mid.microsecond/1000.0))


def deltadatetime(strdatetime=None, days=0, hours=0, minutes=0, seconds=0, milliseconds=0,type="%Y-%m-%d %H:%M:%S"):
    '''
    获取某个时间间隔后的日期时间
    :param strdatetime: 参照日期时间，如果不填则使用当前日期时间
    :param days:间隔的天数，默认0
    :param hours:间隔小时数，默认0
    :param minutes:间隔的分钟数，默认0
    :param seconds:间隔的秒数，默认0
    :param milliseconds:间隔的毫秒数，默认0
    :param type:参照日期时间格式和输出的日期时间格式
    :return:str
    '''
    order_millis = 0
    if strdatetime==None:
        order_millis = nowmillitimetag()
    else:
        order_millis = datetime2millitimetag(strdatetime,type)
    delta = days*24*60*60*1000+hours*60*60*1000+minutes*60*1000+seconds*1000+milliseconds
    return timetag2datetime(order_millis+delta)