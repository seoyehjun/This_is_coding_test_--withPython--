#4:50
from datetime import time
from datetime import date
from datetime import timedelta
from datetime import datetime

N = int(input())

now = datetime.combine(date(1,1,1),time(hour=0, minute=0, second=0))
one_second = timedelta(seconds=1)

print(str(now), type(str(now)))
count =0

goal_time = time(N, 59, 59)
print(type(now.time()),type(goal_time))
while now.time() !=goal_time:
    if '3' in str(now):
        count += 1
    now = now + one_second

print(count)