# Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы.

from itertools import groupby

names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

def dicionary (array):
    keyfunc = lambda x:x[0]
    tasks = sorted(names, key=keyfunc)
    dic = {k: list(j) for k, j in groupby(tasks , key=keyfunc)}
    return dic

print(names)
print(dicionary(names))

