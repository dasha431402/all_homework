 #pylint: skip-file

# -------------- Arifmetic operations --------------
"""
Напишите функцию, которая возвращает true, если число является четным.
"""
def is_odd(n: int):
    if n%2==0:
        return False
    else:
        return True

assert (is_odd(8)) == False
assert not (is_odd(8)) == True
print("all tests passed")


"""
Напишите функцию, которая возращает true, если число является простым
"""
def is_prime(n:int):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

assert (is_prime(8)) == False
assert not (is_prime(10)) == True
assert (is_prime(11)) == True
print("all tests passed")


"""
Напишите функцию, которая возвращает true, если
три заданных числа (в указанном порядке) являются последовательными членами
арифметической прогрессии
"""
def is_arifm_progression(a: int, b: int, c: int):
    if (b-a)==(c-b):
        return True
    return False

assert (is_arifm_progression(2,4,6)) == True
assert not (is_arifm_progression(2,4,6)) == False
assert (is_arifm_progression(2,1,-1)) == False
print("all tests passed")


# -------------- If condition --------------
"""
    Напишите функцию, которая принимает три положительных числа и 
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""
def get_triangle_kind(a: int, b: int, c: int):
    if a <= 0 or b <= 0 or c <= 0:
        return "Ошибка"

    if a == b and a==c and b==c:
        return "Равносторонний"

    elif a == b or a == c or b == c:
        return "Равнобедренный"

    else:
        return "Обычный"


assert (get_triangle_kind(4,4,4)) == "Равносторонний"
assert (get_triangle_kind(4,4,1)) == "Равнобедренный"
assert (get_triangle_kind(4,5,1)) == "Обычный"
assert (get_triangle_kind(0,5,1)) == "Ошибка"
assert (get_triangle_kind(-2,5,1)) == "Ошибка"
print("all tests passed")
