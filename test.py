from dtutils import *

if __name__=="__main__":
    print(nowdatetime('%Y-%m-%d %H:%M:%S.%f'))
    print(nowdate())
    print(nowtime())
    print(nowtimetag())
    print(nowmillitimetag())
    print(timetag2datetime(nowmillitimetag()))
    time.sleep(5)
    print(timetag2datetime(nowtimetag()))
    nowstr = timetag2datetime(nowmillitimetag(), '%Y%m%d %H%M%S.%f')
    print(nowstr)
    print(datetime2timetag(nowstr,type='%Y%m%d %H%M%S.%f'))
    print(datetime2millitimetag(nowstr, type='%Y%m%d %H%M%S.%f'))
    print(deltadatetime(nowstr,hours=-10,seconds=-150,type='%Y%m%d %H%M%S.%f'))
