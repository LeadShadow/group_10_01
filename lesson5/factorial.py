# рекурсія

#  3! -> 3 * 2! -> 3 * 2 * 1! -> 3 * 2 * 1
#  4! -> 4 * 3! -> 4 * 3 * 2! -> 4 * 3 * 2 * 1! -> 4 * 3 * 2 * 1
a = 10


def factorial(n: int):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


