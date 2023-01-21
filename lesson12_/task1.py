from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

print(current_datetime.date())
print(current_datetime.time())
date1 = datetime(year=2018, month=1, day=21, hour=18)
print(date1)
print(current_datetime - date1)

print(current_datetime.weekday())