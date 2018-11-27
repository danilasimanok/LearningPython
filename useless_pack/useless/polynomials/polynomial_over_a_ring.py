"""Многочлены над кольцом."""

from collections import defaultdict
from copy import deepcopy
from ..lists.functions import maxel


class PolynomialException(Exception):
    '''Исключение-обертка для ошибок в использовании многочленов.'''
    pass


class PolynomialOverARingItem:
    '''Многочлен над кольцом.'''

    @staticmethod
    def set_default(def_func):
        '''Установить ноль кольца, над которым построены многочлены.'''
        PolynomialOverARingItem.default = def_func
        PolynomialOverARingItem.coefficients_type = type(def_func())

    @staticmethod
    def set_epsilon(epsilon):
        '''Установить максимальный значимый элемент (тот, что можно округлить до нуля).'''
        PolynomialOverARingItem.epsilon = epsilon

    def __init__(self, d):
        self.d = defaultdict(PolynomialOverARingItem.default)
        for k, v in d.items():
            if (not isinstance(k, int))or k < 0:
                raise PolynomialException(
                    "Степень x должна быть натуральным числом или нулем.")
            if not isinstance(v, PolynomialOverARingItem.coefficients_type):
                raise PolynomialException(
                    "Многочлен не может быть определен над разнородными объектами.")
            else:
                self.d[k] = v
        self.cleanup()

    def __str__(self):
        keys = list(self.d.keys())
        keys.sort(reverse=True)
        s = ""
        for k in keys:
            s += self.d[k].__str__()+"*x^"+k.__str__()+"+"
        return s[0:-1]

    def cleanup(self):
        '''Удалить нулевые коэффициенты.'''
        d = []
        for k in self.d.keys():
            if self.d[k].__abs__() <= PolynomialOverARingItem.epsilon:
                d.append(k)
        for k in d:
            del self.d[k]
        if not self.d[0]:
            self.d[0] = PolynomialOverARingItem.default()
        return self

    def deg(self):
        '''Степень многочлена.'''
        self.cleanup()
        return maxel(list(self.d.keys()))

    def __eq__(self, other):
        self.cleanup()
        other.cleanup()
        if self.deg() != other.deg():
            return False
        for k in self.d.keys():
            if self.d[k] != other.d[k]:
                return False
        return True

    def __add__(self, other):
        if not isinstance(other, PolynomialOverARingItem):
            raise PolynomialException(
                "Многочлен можно складывать только с другим многочленом.")
        else:
            new_d = deepcopy(self.d)
            for k, v in other.d.items():
                new_d[k] += v
        return PolynomialOverARingItem(new_d)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        s = self.d.copy()
        for k, v in s.items():
            s[k] = -v
        return PolynomialOverARingItem(s)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        deg = self.deg() + other.deg()
        d = {}
        for i in range(0, deg+1):
            d[i] = PolynomialOverARingItem.default()
            for j in range(0, i+1):
                d[i] += self.d[j] * other.d[i-j]
        return PolynomialOverARingItem(d).cleanup()

    def __rmul__(self, other):
        return self * other
