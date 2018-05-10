#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dtstr, tzstr):
    dt = datetime.strptime(dtstr, '%Y-%m-%d %H:%M:%S') #get datetime object
    result = re.match(r'UTC(-|\+)(\d+):\d{2}', tzstr).group(1,2) # get timezone str
    offsetTimeZone = timezone(timedelta(hours = int(result[0]+result[1]))) # make timezone object
    timestap = dt.replace(tzinfo=offsetTimeZone).timestamp() # get timestamp
    return timestap
if __name__ == '__main__':
# 测试:
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('ok')
