# 101010100110101011101010
# 0123456789abcdefg
import re

for i in range(16):
    s = "int: {0:d}; hex:{0:#x}; oct: {0:#o}; bin: {0:#b}".format(i)
    print(s)


for num in range(12):
    print('{:^9} {:^9} {:^9}'.format(num, num**2, num**3))


s = "{name} {last_name}".format(last_name='Samus', name='Oleksandr')
print(s)

print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))
print('pi: {:0.3}'.format(3.1416))
print('{} {:+} {:-} {: }'.format(1, 2, -3, 4))
print("|{:^10}|{:^10}|{:^10}|".format('left', 'center', 'right'))

# search
s = 'I am 18 19 years old'
age = re.search(r'\d+', s)
print(age.group())

# findall
s = 'I bought 7 nuts for 6$ and 10 bolts for 3$'
numbers = re.findall(r'\d+', s, flags=re.IGNORECASE)  # python Python PYThon
print(numbers)

# sub
s = 'blue socks and red shoes'
p = re.sub(r'(blue|white|red)', 'colour', s)
print(p)
