"""
Необходимость использования. Настройка точности
"""
from decimal import Decimal, getcontext

getcontext().prec = 6
result = Decimal(1) / Decimal(7)  # 1 / 7
print(result)
# Decimal(1) + 0.2  НЕ МОЖНА! РІЗНІ ТИПИ
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2)


getcontext().prec = 20
print(Decimal(0.1) + Decimal(0.2))
print(float(Decimal(0.1) + Decimal(0.2)) == 0.3)

print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))
print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3) + Decimal(0))

f = 0.2 + 0.1 + 0.3 - 0.5
df = Decimal('0.1') + Decimal('0.2') + Decimal('0.3') - Decimal('0.5')
print(df)


not_precision = Decimal('0.1') / Decimal('0.3')
print(not_precision)

getcontext().prec = 1
precision = Decimal('0.1') / Decimal('0.3')
print(precision)