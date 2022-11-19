# Пусть нам необходимо создать рассылку приглашений на мероприятие.
# Сообщение для каждого участника одинаковое, нам необходимо менять только имя приглашенного.
# Вполне очевидно, что для формирования такого сообщения, лучше использовать функцию.
# Создайте функцию invite_to_event, которая принимает имя приглашенного username и
# будет возвращать f-строку:

# "Dear {username}, we have the honour to invite you to our event".


def invite_to_event(username):
    return f'Dear {username}, we have the honour to invite you to our event'


print(invite_to_event('Sasha'))
