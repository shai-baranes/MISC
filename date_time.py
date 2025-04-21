# from 'Code Bro': https://www.youtube.com/watch?v=ix9cRaBkVe0&t=31709s
import datetime
from datetime import datetime as dt
# from datetime import datetime

date = datetime.date(2025, 1, 2)
print(date)
# 2025-01-02

today = datetime.date.today()

time = datetime.time(12, 30, 0)


print(time)
# 12:30:00


import time
t1 = dt.now()
print(f"{t1} - is now!") # 2025-04-21 16:41:24.188403 - is now!
time.sleep(1)
t2 = dt.now()

print(f"{(t2-t1).total_seconds()} seconds elapsed!")

####### string formatting

print(t1.strftime("%H:%M:%S")) # '16:43:50'
t1 = t1.strftime("%H:%M:%S %Y-%m-%d") # '16:45:19 2025-04-21'

target_datetime = dt(2023, 1, 2, 12, 30, 1)
current_datetime = dt.now()

if target_datetime < current_datetime:
	print("Target date has passed!")
else:
	print("Target date has not passed")

# Target date has passed

