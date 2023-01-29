from datetime import datetime, MINYEAR

date = datetime.now()
print(MINYEAR)
print(date.toordinal())
print(date.timestamp())  # 01.01.1970

print(date.ctime())
print(date.isoformat(sep='T'))

day = date.toordinal()
iso = date.isoformat(sep='T')
sec = str(date.timestamp())
restore_date_from_day = datetime.fromordinal(day)
print(restore_date_from_day.date())
restore_date_from_iso = datetime.fromisoformat(iso)
print(restore_date_from_iso)
restore_date_from_sec = datetime.fromtimestamp(float(sec))
print(restore_date_from_sec)

