import time
from datetime import datetime

date_time = datetime.now()
Date = '%s/%s/%s' % (date_time.day, date_time.month, date_time.year)
Time = '%s:%s:%s' % (date_time.hour, date_time.minute, date_time.second)
Temperature = [Time + " " + Date, 1]
print(Temperature)
