from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)


current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())

d1 = datetime(year=2012, month=1, day=7, hour=14)
print(d1)

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.weekday())

current_datetime = datetime.now()

# next_month = datetime.now()
# next_month += 1

# print(current_datetime < next_month)

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)
print(difference.total_seconds())
