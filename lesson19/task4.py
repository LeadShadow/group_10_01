# Closures

# Особенность существования вложенных локальных пространств имен и тот факт, что они
# создаются динамически,
# дает возможность использовать механизм замыканий в Python.


def greeting(name):
    def message(msg):
        return f'{name} - {msg}'
    return message


msg_for_sasha = greeting('Sasha')

print(msg_for_sasha('Go to home!'))