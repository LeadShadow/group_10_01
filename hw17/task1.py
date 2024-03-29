# Вернемся к задаче о системе оценок в университете, которая имеет следующий вид:
#
# Оценка	Баллы	Оценка ECTS	Объяснение
# 1	0-34	F	неудовлетворительно
# 2	35-59	FX	неудовлетворительно
# 3	60-66	E	достаточно
# 3	67-74	D	удовлетворительно
# 4	75-89	C	хорошо
# 5	90-95	В	очень хорошо
# 5	96-100	A	отлично
# В прошлый раз мы реализовали две функции. Первая — get_grade, принимает ключ в оценке ECTS и
# возвращает соответствующую пятибалльную оценку (первый столбик таблицы). Вторая — get_description,
# тоже принимает ключ в оценке ECTS, но возвращает объяснение оценки в текстовом формате
# (последний столбик таблицы). На несуществующий ключ функции должны возвращать значение None.
#
# Реализуйте функцию высшего порядка get_student_grade, которая принимает параметр option.
# Если он равен значению "grade", то функция возвращает функцию get_grade, а если его значение
# равно "description", то возвращает функцию get_description. Если параметр по значению не
# совпал с заданными, то функция get_student_grade должна возвращать значение None.

def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description


if __name__ == '__main__':
    func = get_student_grade('description')
    print(func('A'))