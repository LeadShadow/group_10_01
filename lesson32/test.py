import pickle
import json
# expenses = {
#     'hotel': 600,
#     'breakfast': 150,
#     'taxi': 150,
#     'lunch': 200
# }
#
# file_name = 'expenses.txt'
# with open(file_name, 'w', encoding='utf-8') as file:
#     for key, value in expenses.items():
#         file.write(f'{key}|{value}\n')

# expenses = {}
# file_name = 'expenses.txt'
# with open(file_name, 'r', encoding='utf-8') as file:
#     raws_expenses = file.readlines()
#     for line in raws_expenses:
#         key, value = line.split('|')  # 'hotel|600' -> ['hotel', '600']
#         expenses[key] = int(value)
#
# print(expenses)

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

byte_string = pickle.dumps(some_data)
print(byte_string)
unpacked = pickle.loads(byte_string)
print(some_data == unpacked)
print(some_data is unpacked)

file_name = 'data.bin'
with open(file_name, 'wb') as file:
    pickle.dump(some_data, file)

with open(file_name, 'rb') as file:
    unpacked = pickle.load(file)

print(unpacked)

some_data = {
    'key': 'value',
    2: [1, 2, 3],
    'tuple': (5, 6),
    'a': {'key': 'value'}
}

byte_string = json.dumps(some_data)
print(byte_string)
unpacked = json.loads(byte_string)
print(some_data == unpacked)
print(some_data is unpacked)

file_name = 'data.json'
with open(file_name, 'w') as file:
    json.dump(some_data, file)

with open(file_name, 'r') as file:
    unpacked = json.load(file)

print(unpacked)