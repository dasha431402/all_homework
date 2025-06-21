"""-----------------------Функция all, any---------------------"""
def more_fifth (lst):
    return all(n>50 for n in lst)


print(more_fifth([51,65,70,20]))
print(more_fifth([51,65,70,89]))


def anymore_fifth (lst):
    return any([n>50 for n in lst])

print(anymore_fifth([5,51,7,2]))

#print(more_fifth([1,5,70,8]))
print("Филтер")
"""-----------------------Функция filter---------------------"""

"""numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]

def condition(number): return number > 1

result = filter(condition, numbers)

for n in result:
    print(n, end=" ")
    
    Для фильтрации определяем функцию condition, в которую в качестве параметра передается каждый элемент списка numbers.
     Результатом функции являет True, если число больше 1, либо False, если число меньше 2.
     Результатом функции filter является отфильтрованные значения из списка, то есть те числа, которые больше 1.
     Вместо определения отдельной функции-условия, если условие короткое, удобно в подобных случаях использовать лямбда-выражения:
numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
 
result = filter(lambda n: n > 1, numbers)
 
for n in result: print(n, end=" ")      # 2 3 4 5"""


lst = [0,9,-5,7,4,-6]
result = filter(lambda n: n>0 or n==0, lst) #условие сразу через лямбду и список, на которое это условие применить

for n in result:
    print(n, end=" ")




lst = [1,2,4,6,5,10]
b= filter(lambda x: x%2==0, lst)
for x in b:
    print(x)


def is_prost(x):
    d=x-1
    if d<0:
        return False

    while d>1:
        if x%d==0:
            return False
        d-=1
    return True

b= filter(is_prost,lst)
lst= tuple(b)
print(lst)


lst = [2,3,4,5,6,7,8,0]
def is_odd(lst):
    return n%2==0
b=filter(is_odd,lst)
for n in b:
    print(n)




