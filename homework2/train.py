import math

print("Hello word!")

lst = [1, 3, 5, 7, 9]


def arifm(lst):
    d = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != d:
            return False
    return True


"""Напишите функцию, которая возвращает true, если все заданные числа (в указанном порядке) 
являются последовательными членами арифметической прогрессии"""

"""
def arifmetic(lst_numbers):  # список
    delta = lst_numbers[1] - lst_numbers[0]  # разница для арифм, 3-1=2
    for i in range(len(lst_numbers) - 1):  # нам нужно получить диапазон до посл числ в списке не вкл
        # <- подсчет длины списка и минус 1, тк индекс дб меньше на единицу (если длина 5 шт, то индекс от 0 до 4)
        if lst[i + 1] - lst[i] != delta:
            return False
    return True


assert (arifmetic([1, 3, 5, 7, 9])) == True
"""
"""
    Дана строка, разбить ее на слова. Слова разделены одним пробелом
    "Александр Сергеевич Пушкин" -> ["Александр", "Сергеевич", "Пушкин"]
"""


def get_words(s):
    return s.split(" ")


assert (get_words("Александр Сергеевич Пушкин")) == ["Александр", "Сергеевич", "Пушкин"]


def isgeom(lst):  # Геометрич прогрессия?
    i = 0
    el = lst[i + 1] / lst[i]  # второе число делим на первое, чтобы получить частное; можно сразу записать в Если
    for num in lst:
        if lst[i + 2] / lst[i + 1] == el:  # если второе разделить на первое = третье разделить на второе, то геом прог
            return "Это геометр прогрессия"
    return "Это не геом прогрессия"


print(isgeom([1, 2, 4, 8, 16]))


# все числа до 100, делятся на 3 и 5
def three_five(max_n):
    for el in range(max_n):
        if el % 3 == 0 and el % 5 == 0:
            print(el)


print(three_five(100))


lst = [10,20,30,40] # 1)посчитали кол-во эл в списке 2)чтобы i перебирался по индексам от 0 вкл до 3 вкл
for i in range(len(lst)):
    print(lst[i])           #выводит список по индексу


def have_null(lst):    #сообщение, если список содержит нули
    for el in lst:
        if el == 0:
            print("Есть нули")
            break
        #print("Нет нулей")
    if  el!=0:
        print("Нет нулей")
print(have_null([1,2, 3,4,3,5]))

def all_null(lst):             #true если все в списке нули
    i=0
    for i in range(len(lst)):
        if lst[i]!=0:
            return False
    return True
range(len(lst)) #5 -- 0,1,2,3,4
print(all_null([0,0,0,0,0,0]))

def all_null(lst):
    for el in lst:
        if el!=0:
            return  False
    return True

print(all_null([0,0,0,0,0,0]))

def del_num (lst, num):
    for el in lst:
        if el==num:
            lst.remove(el)
    return lst

print(del_num([1,2,3,4],4))
print("-----------------------------------------")

def all_el_same(lst):#true если все значения в списке одинаковые
    i=1
    for i in range(len(lst)):
        if lst[i] != lst[i-1]:
            return False            #сравнивать первый со вторым
    return True
print(all_el_same([1,0,1,1]))

def all_el_same(lst):
    for el in lst[1:]:
        if el !=lst[0]:
            return False
    return True

print(all_el_same([1,0,1,1]))


def is_list_descending(lst):
    for el in lst[1:]:
        if el>=lst[0]:
            return False
    return True
print(is_list_descending([5,5,4,1]))


def is_list_descending(lst):
    for i in range(len(lst)-1):
        if lst[i] <=lst[i+1]:
            return False
    return True
print(is_list_descending([8,5,4,1]))


def no_duplicat(lst):
    res = []
    for el in lst:
        if el not in res:
            res.append(el)
        if el in lst:
            continue
    return res
print(no_duplicat([1,1,5,5,7,7]))


def abbrev(s,sep):
    res =[]
    a = ""
    for el in s:
        if el != sep:
            a+=el
        else:
            if a !='':
                res.append(a)
            a = ""
    res.append(a)
    return res
print(abbrev("Союз Егорчик  представляет", " "))



def abbrev(s):
    a = s.split(" ")
    return a
print(abbrev("Союз Егорчик представляет"))


def abbrev(s):

    a = list(s)
    d=str(a)
    return d
print(abbrev("Союз Егорчик представляет"))

def move_zeros(lst: list[float]) -> list:
    i = 0
    for el1 in lst:               # название элемента - без разницы, главное, что они разные дб
        j = 0
        if lst[i] == 0:
            for el2 in lst:        # название элемента - без разницы, главное, что они разные дб
                if j > i:
                    if lst[j] != 0 and lst[i] == 0:
                        lst[i], lst[j] = lst[j], lst[i]
                j += 1
        i += 1
    return lst
print(move_zeros([0,1,3,0,0,0,6,7,0]))

def move_zeros(lst):
    for el1 in range(len(lst)-1):        # первый список 5-1-0-0-2-3-0-7 элементы по 0-1-2-3-4-5-6 индексам
        if lst[el1] ==0:                  # второй список 5-1-0-0-2-3-0-7 элементы по 0-1-2-3-4-5-6 индексам
            for el2 in range(len(lst)-1):
                if el2>el1:
                    if lst [el2]!=0 and lst [el1]==0:
                        lst[el1], lst[el2] = lst[el2], lst[el1]
    return lst

print(move_zeros([0,1,3,0,0,0,6,7,0]))



















print("-------------------------------------------------------")
def uravnenie(a, x):
    return abs(x ** 5 + abs(a * x - x ** 3) - a) + a * (x ** 2) + a ** 8


print(uravnenie(1, 0))


def chetir(b):
    chet = str(b)  # 3,4,5
    chet = chet[-1] + chet
    return chet


print(chetir(345))


def cosx(x):
    return math.cos(x) + pow((math.cos(x)), 2) / ((x - 1) ** 0.5) + math.sin(x) / math.cos(x)


print(round(cosx(10), 4))


def logx(x):
    return math.log(pow(x, 3)) + pow(2, x - 2)


print(round(logx(10), 4))
"""-------------------------------------------------------------------------------------------------"""


def summ(d):
    s = 0  # сумма
    for el in d:
        s = s + int(el)
    return s


print(summ("1234"))


def first_num(d):
    return d[0]


print(first_num("6463"))


def izmena(d):
    e = d[-1] + d[1:-1] + d[0]
    return e


print(izmena("5647"))


def vvod(d):
    d = int(d)
    while d >= d + 1 and d != 100:
        print("Введите число: ")
    return "ok"


print(vvod("2"))
