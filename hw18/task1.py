# В модуле 5 мы писали функцию sanitize_phone_number для нормализации строки с телефонным номером. Напомним, что при получении строк
#
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# Мы получали следующий вывод:
#
# 380501233234
# 0503451234
# 0508889900
# 380501112222
# 380501112211
# Представьте, что в другом месте программы у нас появилось требование сделать вывод в формате
#
# +380501233234
# +380503451234
# +380508889900
# +380501112222
# +380501112211
# В этом случае идеально подойдет создание декоратора для функции sanitize_phone_number.
# Декоратор должен добавлять для коротких номеров префикс +38, а для полного международного
# номера (из 12 символом) — только знак +. Реализуйте декоратор format_phone_number для
# функции sanitize_phone_number с необходимым функционалом.
def format_phone_number(func):
    def wrapper(phone):
        new_phone = func(phone)
        if len(new_phone) == 10:
           new_phone = "+38" + new_phone
        elif len(new_phone) == 12:
           new_phone = "+" + new_phone
        return new_phone
    return wrapper


@format_phone_number
def sanitize_phone_num_ber(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone



print(sanitize_phone_num_ber("38050 111 22 11"))

