# На 6 занятті мы решали задачу нормализации данных. Давайте расширим ее. При анализе данных
# часто возникает необходимость избавиться от экстремальных значений, прежде чем начать работать с
# данными дальше. Напишите функцию data_preparation, которая принимает набор данных, список списков
# (Пример: [[1,2,3],[3,4], [5,6]]). Функция должна удалять из переданных списков наибольшее и
# наименьшее значение, но только если размер списка больше двух элементов. После удаления данных
# из каждого списка, необходимо слить их вместе в один список, отсортировать его в порядке убывания
# и вернуть полученный список в качестве результата (Для примера выше результат будет следующим:
# [6, 5, 4, 3, 2]).


def data_preparation(list_data: list) -> list:
    result = []
    for sub_list in list_data:
        if len(sub_list) >= 3:
            sub_list.remove(min(sub_list)) # min(sub_list) -> 1
            sub_list.remove(max(sub_list)) # max(sub_list) -> 3
            # [1, 2]
        result.extend(sub_list) # -> [].extend([1,2]) -> [1, 2]
    return sorted(result, reverse=True) # 6, 5, 4, 3, 2


if __name__ == "__main__":
    print(data_preparation([[1,2,3],[3,4], [5,6]]))