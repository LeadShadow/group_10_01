# У нас є три логічні змінні.
# Перша визначає статус користувача is_active, що дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу. True or False
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

# Надайте змінної access, значення, яке покаже, чи є доступ користувача. Використовуйте логічні оператори.

# Адміністратор завжди має доступ незалежно від значень змінних is_admin і is_active.

# Користувач має доступ тільки якщо is_permission дорівнює True і is_active також дорівнює True

is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_admin_1 = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))
# пуста строка -> False
access = is_permission and is_active or is_admin
print(is_active and is_admin and is_admin_1)
print(is_active or is_admin)
print(is_permission and is_admin)
print(is_permission or is_admin)


