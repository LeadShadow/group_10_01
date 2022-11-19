def apply_discount(discount: str):
    if len(discount) == 1:
        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        discount = '0.' + discount[0]
    elif len(discount) == 2:
        discount = '0.' + discount[0] + discount[1]
    elif len(discount) == 3:
        discount = '0.' + discount[0] + discount[1] + discount[2]
    return float(discount)


def discount_price(price, discount):
    def apply_discount():
        nonlocal price, discount
        return price * discount
    price = apply_discount()
    return price


# 45% -> 0.55
# 50% -> 0.5
# 20% -> 0.8
user_input = input('Input discount: ')
discount = apply_discount(user_input)
print(discount_price(price=100, discount=discount))

