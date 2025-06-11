
# -------------- strings, for loops --------------

"""
    Проверить, является ли строка с пробелами палиндромом (а роза упала на лапу азора).
    Упростим задачу, допуская, что cлова в предложении разделяются только одним пробелом.
"""
def is_palindrome(s: str) -> bool:
    words = s.split()
    s="".join(words)
    if s != s [::-1]:
        return False
    return True

assert (is_palindrome("а роза упала на лапу азора")) == True
assert not (is_palindrome("а роза упала на лапу азора")) == False
print("all tests passed")


"""
    Дана строка, разбить ее на слова. Слова разделены одним пробелом
    "Александр Сергеевич Пушкин" -> ["Александр", "Сергеевич", "Пушкин"]
"""
def get_words(string: str, sep: str) -> list[str]:
    res = []
    curr_part = ""
    for s in string:
        if s != sep:
            curr_part += s
        else:
            res.append(curr_part)
            curr_part = ""
    if curr_part != "":
        res.append(curr_part)
    return res

assert (get_words("Александр Сергеевич Пушкин", " ")) == ["Александр", "Сергеевич", "Пушкин"]
print("all tests passed")


"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""
def get_person_short_name(fio: str) -> str:
    parts = fio.split()
    fam = parts [0]
    first_initial = parts [1] [0]
    second_initial = parts [2] [0]

    return f"{fam} {first_initial}. {second_initial}."

assert (get_person_short_name("Лермонтов Михаил Юрьевич")) == "Лермонтов М. Ю."
print("all tests passed")
