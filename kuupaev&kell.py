from datetime import datetime
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_second = now.second
print str(current_day) + "/" + str(current_month) + "/" + str(current_year) + " " + str(current_hour) + ":" + str(current_minute) + ":" + str(current_second)

print ""

import time
Time = str(time.strftime ('%H:%M:%S'))
Date = str(time.strftime ('%a %d.%m.%Y'))
print Date + " " + Time
