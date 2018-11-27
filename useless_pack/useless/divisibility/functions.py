"""Некоторые функции, связанные с делимостью чисел."""


def number_is_prime(n):
    '''Проверка простоты числа.'''
    if (n % 2 == 0 and n != 2) or n == 1:
        return False
    i = 3
    e = n**0.5
    while i <= e:
        if n % i == 0:
            return False
        i += 2
    return True


def extended_Euclid(a, b):
    '''Расширенный алгоритм Евклида.'''
    if a == 0:
        return (b, 0, 1)
    g, x, y = extended_Euclid(b % a, a)
    return (g, y-(b//a)*x, x)
