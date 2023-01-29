# random.seed([x]) -> ініціалізація генератора випадкових чисел
# random.random() -> випадкове число від 0 до 1
# random.randrange(start, stop, step) -> повертає випадково вибране число з послідовності
# random.randint(x, y) -> випадкове число N x <= N <= y
# random.choice(sequence) -> випадковий елемент непустої послідовності
# random.shuffle(sequence, [rand]) -> перемішування послідовності(незмінна послідовність)
# random.sample(population, k) -> список довжиною k з послідовності population

import random as r

r.seed()
print(r.random())
print(r.randint(1, 10))

for _ in range(10):
    print(r.randint(1, 10), end=' ')

print('\n')
l = list(range(1, 37))
print(l)

r.shuffle(l)
print(l)

print(r.choice(l))
print(r.sample(l, k=5))
