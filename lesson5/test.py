some_dict = {
    'курс долара': 40.1,
    1: 'one'
}
my_tuple = (1, 2, 3, 4)
print(some_dict.get('курс долара', 30))
print(my_tuple[1])

for i in my_tuple:
    print(i)


for v in some_dict.values():
    print(v)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list1:
    print(type(i))

print(list1[-1])
print(list1[0:5])
my_string = 'This is awesome string'
print(my_string[5:10])
odd_numbers = list1[0::2]
even_numbers = list1[1:10:2]
three_numbers = list1[2:10:3]
print(odd_numbers)
print(even_numbers)
print(three_numbers)
list_copy = list1[:]
print(list_copy)
print(list1)


list1.append(5)
list1.append(5)
list1.append(5)
numbers_5 = list1.pop(5)
print(list1)
list2 = ['a', 'b']

list1.extend(list2)
print(list1)

list1.insert(0, 0)
ind_0 = list1.index('a')
print(ind_0)
print(list1)
count_5 = list1.count(5)

list_alfavit = ['z', 'a', 'b', 'i', 'g', 'e', 'c']
list_alfavit.sort(reverse=True)
print(list_alfavit)
print(count_5)
