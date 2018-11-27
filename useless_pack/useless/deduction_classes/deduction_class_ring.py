"""Кольцо вычетов по модулю."""


class DeductionClassException(Exception):
    '''Исключение-обертка для ошибок в использовании классов вычетов.'''
    pass


class DeductionClass:
    '''Класс вычетов a по модулю m.'''

    def __init__(self, a, m):
        if not(isinstance(m, int) and m > 1):
            raise DeductionClassException(
                "Модуль должен быть натуральным числом, большим единицы.")
        elif not isinstance(a, int):
            raise DeductionClassException(
                "Класс вычетов должен быть целым числом.")
        else:
            self.m = m
            self.a = a % m

    def __str__(self):
        return "["+str(self.a)+"]"+str(self.m)

    def __eq__(self, other):
        return (self.a == other.a)and(self.m == other.m)

    def __add__(self, other):
        if not isinstance(other, DeductionClass):
            raise DeductionClassException(
                "Класс вычетов можно складывать только с классом вычетов.")
        if self.m == other.m:
            return DeductionClass(self.a + other.a, self.m)
        raise DeductionClassException(
            "Складывать можно только классы вычетов по одному модулю.")

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return DeductionClass(-self.a, self.m)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, DeductionClass):
            raise DeductionClassException(
                "Класс вычетов можно умножать только на класс вычетов.")
        if self.m == other.m:
            return DeductionClass(self.a * other.a, self.m)
        raise DeductionClassException(
            "Перемножать можно только классы вычетов по одному модулю.")

    def __rmul__(self, other):
        return self * other
