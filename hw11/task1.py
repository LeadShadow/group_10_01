# Створити функцію get_days_from_birthday(date: datetime). Використовуючи модуль datetime,
# знайти кількість днів від вашої дати народження до теперішньої дати

from datetime import datetime
def get_days_from_birthday(date: datetime):
    gebursTagdate = datetime(year=2008, month=5, day=27)
    return (date - gebursTagdate).days

# gaburstag = datetime(year=2023, month=5, day=27)
# deferens = gaburstag - date
# print(deferens)
if __name__ == "__main__":
    date = datetime.now()
    print(get_days_from_birthday(date))