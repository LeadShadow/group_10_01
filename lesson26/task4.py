# Перепишем задачу расчета задолженностей по коммунальным услугам с помощью класса UserList.
#
# payment = [1, -3, 4]
#
#
# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum = sum + value
#     return sum
# Напомним условие. У нас есть список показаний задолженностей по коммунальным услугам в конце месяца —
# список payment. Задолженности могут быть отрицательными — у нас переплата, или положительными,
# если необходимо оплатить по счетам.
#
# Создайте класс AmountPaymentList, наследуйте его от класса UserList. Сделайте функцию amount_payment
# методом класса AmountPaymentList.
from collections import UserList

class AmountPaymentList(UserList):
    def amount_payments(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum


amount = AmountPaymentList()
amount.data = [100, -200, -300, 100, 150, 200, 250]
print(amount.amount_payments())
