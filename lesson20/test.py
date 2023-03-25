# def handle_operation(x, y, operator):
#     if operator == '-':
#         return x - y
#     elif operator == '+':
#         return x + y
#
#
# print(handle_operation(10, 5, '-'))
# print(handle_operation(10, 5, '+'))


def complicated(x, y):
    return x / y


def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


complicated = logged_func(complicated)
print(complicated(10, 20))


def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


# декоратор
@logged_func
def complicated(x, y):
    return x / y


print(complicated(10, 20))


# Ітератори і генератори


def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10)

print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))

# example
x = 4

def sum_x(y):
    global x
    while x <= y:
        x += 1
        return x


print('------------------------')
print(sum_x(10))
print(sum_x(10))
print(sum_x(10))
print(sum_x(10))
print(sum_x(10))
print(sum_x(10))
print('------------------------')
def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10)
for i in five_to_ten_generator:  # for i in range(5, 11)
    print(i)
print('------------------------')
for i in range(5, 11):
    print(i)


sum_lambda = lambda x, y: x + y


numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)

print('--------')
