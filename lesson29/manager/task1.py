"""
Для того, чтобы объект можно было использовать в конструкции with ... as ...: в объекте должны быть определены два
метода: __enter__, __exit__.
__enter__ -- метод, который принимает только один аргумент self. Если метод что-то возвращает, то его вывод будет
записан в переменную val в конструкции with context_manager as val:.
__exit__ -- обязательно принимает 4 аргумента: self, exception type, exception value, exception traceback.
Эти аргументы нужны для корректной обработки исключений внутри __exit__.
"""