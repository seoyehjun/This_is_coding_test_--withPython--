from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

now_date = date(year= 2140, month=4, day= 11)
now_time = time(hour=0, minute=12, second=0)
now_datetime = datetime.combine(date(200,1,1),now_time)

print(now_datetime, type(now_datetime))
print(now_datetime.time(),type(now_datetime.time()))
print(bool(-1))