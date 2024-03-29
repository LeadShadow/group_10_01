# Разработайте функцию get_days_from_today(date), которая будет возвращать количество дней
# от текущей даты, где параметр date — это строка формата '2020-10-09' (год-месяц-день).

# Зробити переведення в об'єкт datetime і зробити обрахунки к-сті днів
from datetime import datetime

def get_days_from_today(date):
    current_date = datetime.now().date()
    import_date = datetime.strptime(date, '%Y-%m-%d').date()
    delta = current_date - import_date
    return delta.days



print(get_days_from_today('2020-11-28'))