# datetime.today() -> об'єкт datetime з теперішньої дати і часу
# datetime.fromtimestamp(timestamp) -> дата з стандартного представлення часу
# datetime.now() -> об'єкт datetime з теперішньої дати і часу
# datetime.combine(date, time) -> об'єкт datetime з комбінації date і time
# datetime.strptime(date_string, format) -> перетворення рядка в datetime
# datetime.strftime(format) -> рядок з datetime об'єкту
# datetime.date() -> об'єкт дати
# datetime.time() -> об'єкт часу
# datetime.replace(year, month, day ...) -> повертати новий об'єкт datetime з зміненими атрибутами
# datetime.weekday() -> день тижня в вигляді числа
# datetime.isoformat(sep='T') -> гарний рядок вигляду 'YYYY-MM-DDTHH:MM:SS:mmmmmm'

from datetime import datetime

# Створення дат
date = datetime(year=2023, month=1, day=28, hour=17, minute=15)
print(date)
print(date.date())
print(date.time())

print(datetime.now())
print(datetime.today())


# Переведення в дату і назад 28.01.2023
string_date = '28-01-2023'
date = datetime.strptime(string_date, '%d-%m-%Y')
print(type(string_date))
print(type(date))
other_date = date.replace(month=3, day=10)
print(other_date)
str_date = other_date.strftime('%Y-%m-%d')
print(str_date)
