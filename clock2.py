import time
import calendar

while True:
    total_seconds = calendar.timegm(time.gmtime())
    total_minutes = total_seconds // 60
    total_hours = total_minutes // 60
    print(total_hours % 24,":", total_minutes % 60,":", total_seconds % 60)
    time.sleep(1)
