# -------------- lists --------------

"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""
def is_list_growing(lst: list[float]) -> bool:
    for i in range (1,len(lst)):
        if lst [i] <= lst[i-1]:
            return False
    return True

assert (is_list_growing([1.2, 1.4, 2.5, 3.1])) == True
assert not (is_list_growing([1.2, 1.4, 2.5, 0.1])) == True
assert (is_list_growing([1.2, 1.4, 2.5, 0.1])) == False
print("all tests passed")

"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""

def get_pairs_number(lst: list[int], n) -> list[tuple]:
    pairs = []
    i=0
    for _ in lst:
        if (len(lst) > i+1) and (lst[i] + lst[i+1]) == n:
            el = (lst[i], lst[i + 1])
            pairs.append(el)
        i+=1
    return pairs

assert (get_pairs_number([1, 2, 4, 3, 5, 2], 8)) == [(3,5)]
assert (get_pairs_number([1, 2, 4, 3, 5, 2], 6)) == [(2,4)]
assert (get_pairs_number([1, 2, 4, 3, 5, 2], 7)) == [(4,3), (5,2)]
assert (get_pairs_number([1, 2, 4, 3, 5, 2], 7)) == [(4,3), (5,2)]
print("all tests passed")

