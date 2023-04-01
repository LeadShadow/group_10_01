for i in filter(lambda x: x % 2, range(1, 11)):
    print(i)


def find_add_numbers():
    for i in range(1, 11):
        if i % 2:
            print(i)


find_add_numbers()


some_str = 'aaAbbB C F DDd EEe'
for i in filter(lambda x: x.islower(), some_str):
    print(i)

def is_letter_lower():
    for x in some_str:
        if x.islower():
            i = x
            print(i)

print('------')
is_letter_lower()