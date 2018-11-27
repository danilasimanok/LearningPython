"""Поле вычетов по модулю."""

from .deduction_class_ring import *
from ..divisibility.functions import number_is_prime, extended_Euclid


class DeductionClassPrime(DeductionClass):
    '''Класс вычетов a по простому модулю m.'''

    def __init__(self, a, m):
        if number_is_prime(m):
            super(DeductionClassPrime, self).__init__(a, m)
        else:
            raise DeductionClassException("Модуль должен быть простым числом.")

    def __add__(self, other):
        return DeductionClassPrime.to_prime(super(DeductionClassPrime, self).__add__(other))

    def __radd__(self, other):
        return DeductionClassPrime.to_prime(super(DeductionClassPrime, self).__radd__(other))

    def __neg__(self):
        return DeductionClassPrime.to_prime(super(DeductionClassPrime, self).__neg__())

    def __sub__(self, other):
        return DeductionClassPrime.to_prime(super(DeductionClassPrime, self).__sub__(other))

    def __mul__(self, other):
        return DeductionClassPrime.to_prime(super(DeductionClassPrime, self).__mul__(other))

    def __rmul__(self, other):
        return DeductionClassPrime.to_prime(super(DeductionClassPrime, self).__rmul__(other))

    def reverse(self):
        '''Обратный к данному.'''
        if self.a != 0:
            t = extended_Euclid(self.a, self.m)
            return DeductionClassPrime(t[1], self.m)
        raise ZeroDivisionError("Не существует обратного к нулю.")

    def __truediv__(self, other):
        return self*other.reverse()

    @staticmethod
    def to_prime(ded_class):
        '''Перевести класс вычетов по любому модулю в класс по простому.'''
        if number_is_prime(ded_class.m):
            return DeductionClassPrime(ded_class.a, ded_class.m)
        raise DeductionClassException("Модуль должен быть простым числом.")
