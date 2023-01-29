from datetime import datetime, timedelta


date = datetime.now()
interval = timedelta(days=30)
finish = date + interval
print(finish.date())
