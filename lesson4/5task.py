user_input = input('Input discount: ')


def apply_discount(discount: str):
    if len(discount) == 1:
        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        discount = '0.' + discount[0]
    elif len(discount) == 2:
        discount = '0.' + discount[0] + discount[1]
    elif len(discount) == 3:
        discount = '0.' + discount[0] + discount[1] + discount[2]
    return float(discount)


print(apply_discount(user_input))
