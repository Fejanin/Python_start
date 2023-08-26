# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

print('Задача без звездочек.')
def is_included_in_the_range1(lst: list, min_n: int, max_n: int) -> list:
    res = []
    for i in range(len(lst)):
        if min_n <= lst[i] <= max_n:
            res.append(i)
    return res

# ТЕСТЫ(1)
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(is_included_in_the_range1(lst1, 2, 10))
print(is_included_in_the_range1(lst1, 2, 9))
print(is_included_in_the_range1(lst1, 0, 6))
print('-' * 20 + '\n')
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

print('Задача с 1-й звездочкой.')
def is_included_in_the_range2(lst: list, min_n: int, max_n: int) -> list:
    return [i for i in range(len(lst)) if min_n <= lst[i] <= max_n]

# ТЕСТЫ(2)
print(is_included_in_the_range2(lst1, 2, 10))
print(is_included_in_the_range2(lst1, 2, 9))
print(is_included_in_the_range2(lst1, 0, 6))
print('-' * 20 + '\n')
# (**) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

print('Задача с 2-я звездочками.')
def is_included_in_the_range3(lst: list, min_n: int, max_n: int) -> list:
    return [(i, lst[i]) for i in range(len(lst)) if min_n <= lst[i] <= max_n]

lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(is_included_in_the_range3(lst1, 2, 10))
