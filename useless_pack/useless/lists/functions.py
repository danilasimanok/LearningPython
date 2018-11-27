"""Некоторые функции для работы со списками."""

def maxel(lst):
    '''Поиск наибольшего элемента списка.'''
    result = lst[0]
    for element in lst[1:]:
        if result < element:
            result = element
    return result
