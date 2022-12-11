# є випадковий список, потрібно представити його в зворотньому напрямку 
# [1, 3, 5] -> [5, 3, 1]


def reverse_list(list: list) -> list:
    return list[::-1]


print(reverse_list([1, 3, 5]))
