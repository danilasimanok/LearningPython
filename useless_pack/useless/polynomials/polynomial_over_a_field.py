"""Многочлены над полем."""

from .polynomial_over_a_ring import *


class PolynomialOverAFieldItem(PolynomialOverARingItem):
    '''Многочлен над полем.'''

    def __init__(self, d):
        if not hasattr(PolynomialOverAFieldItem.default(), "__truediv__"):
            raise PolynomialException("В поле должен существовать элемент обратный по умножению.")
        super(PolynomialOverAFieldItem, self).__init__(d)

    @staticmethod
    def from_ring_to_field(polynom):
        '''Превращает многочлен над кольцом в многочлен над полем.'''
        return PolynomialOverAFieldItem(polynom.d)

    def __add__(self, other):
        return PolynomialOverAFieldItem.from_ring_to_field(super(PolynomialOverAFieldItem, self).__add__(other))

    def __radd__(self, other):
        return PolynomialOverAFieldItem.from_ring_to_field(super(PolynomialOverAFieldItem, self).__radd__(other))

    def __neg__(self):
        return PolynomialOverAFieldItem.from_ring_to_field(super(PolynomialOverAFieldItem, self).__neg__())

    def __sub__(self, other):
        return PolynomialOverAFieldItem.from_ring_to_field(super(PolynomialOverAFieldItem, self).__sub__(other))

    def __mul__(self, other):
        return PolynomialOverAFieldItem.from_ring_to_field(super(PolynomialOverAFieldItem, self).__mul__(other))

    def __rmul__(self, other):
        return PolynomialOverAFieldItem.from_ring_to_field(super(PolynomialOverAFieldItem, self).__rmul__(other))

    def __truediv__(self, other):
        degree = other.deg()
        res_d = defaultdict(PolynomialOverAFieldItem.default)
        p = PolynomialOverAFieldItem(self.d)
        while p.deg() >= other.deg():
            key = p.deg() - other.deg()
            val = p.d[p.deg()] / other.d[degree]
            res_d[key] = val
            p = p - other * PolynomialOverAFieldItem({key:val})
        return PolynomialOverAFieldItem(res_d)

    def __mod__(self, other):
        div = self / other
        return self-div * other
