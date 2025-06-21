"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""


def get_views_count(n: int) -> str:
    last_el = list(str(n))[- 1]

    if last_el == "1":
        return f'{n} {"просмотр"}'

    if last_el in ['2', '3', '4']:
        return f'{n} {"просмотра"}'

    return f'{n} {"просмотров"}'


assert (get_views_count(130)) == '130 просмотров'
assert (get_views_count(4)) == "4 просмотра"
assert (get_views_count(1)) == "1 просмотр"
print("all tests passed")

"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинуты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции
    (функция ничего не возвращает)

"""


def move_zeros(lst: list[float]) -> list:
    no_zeros = []
    lst.reverse()
    for el in lst:
        if el == 0:
            no_zeros.append(el)
        else:
            no_zeros.insert(0, el)

    return no_zeros


assert move_zeros([5, 6, 0, 4, 0, 0, 2]) == [5, 6, 4, 2, 0, 0, 0]
print("all tests passed")


def move_zeros(lst: list[float]) -> list:
    i = 0
    for el1 in lst:
        j = 0
        if lst[i] == 0:
            for el2 in lst:
                if j > i:
                    if lst[j] != 0 and lst[i] == 0:
                        lst[i], lst[j] = lst[j], lst[i]
                j += 1
        i += 1
    return lst


a = [5, 1, 0, 0, 2, 3, 0, 7]
move_zeros(a)
assert move_zeros(a) == [5, 1,2,3,7, 0, 0, 0]
print("all tests passed")

"""
    Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
    Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
    "Иsвtrан Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"

"""


def clean_name(fio: str) -> str:
    clean = ""
    list_abc = ["в", "а", "н", "б", "г", "д", "е", "ё", "ж", "з", "й", "к", "л", "м", "о", "п", "р", "с", "т", "у", "ф",
                "х",
                "ц", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "ч", "и", " "]
    list_ABC = []
    for el in list_abc:
        list_ABC.append(el.upper())

    for el in list(fio)[:]:
        if el in list_abc or el in list_ABC:
            clean = clean + "" + el
    return clean


assert (clean_name("Иsвtrан Ив^%ан Ива?но)вич")) == "Иван Иван Иванович"
print("all tests passed")

"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]

"""


def get_pct_growth(s: list[float]) -> list[float]:
    res = []
    for i in range(len(s) - 1):
        if i == 0:
            res.append(None)
        a = str(round((s[i + 1] - s[i]) * 100 / s[i])) + "%"
        res.append(a)
    return res


assert (get_pct_growth([100, 150, 300, 400])) == [None, "50%", "100%", "33%"]
print("all tests passed")
