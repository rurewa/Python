# Сравнение списка с кортежем
lst = [10, 20, 30]
print(type(lst), lst.__sizeof__())
for val in lst: # Доступ к списку
    print(val, end = " ")
print("\n") # С новой строки
tpl = (10, 20, 30)
print(type(tpl), tpl.__sizeof__())
for val in tpl: # Доступ к кортежу
    print(val, end = " ")
print("\n")
# Создание кортежей 2-мя способами
a_tuple = ()
print(type(a_tuple))
b_tuple = tuple()
print(type(b_tuple))
# Кортеж с заданных содержанием создаётся как список,
# только с круглыми скобками
a_tuple = (15, 'e', 500)
print(a_tuple)
# Или тоже самое, но с функцией tuple
a_tuple = tuple((15, 'e', 500))
print(a_tuple)
