# Сравнение размера а байтах списка с кортежем
lst = [10, 20, 30]
print(type(lst), lst.__sizeof__())
for val in lst: # Доступ к списку
    print(val, end = " ")
print("\n") # С новой строки
tpl = (10, 20, 30)
print(type(tpl), tpl.__sizeof__())
for val in tpl: # Доступ к кортежу
    print("Доступ к кортежу:", val, end = " ")
print("\n")
# Создание кортежей 2-мя способами
a_tuple = ()
print(type(a_tuple))
b_tuple = tuple()
print(type(b_tuple))
# Кортеж с заданным содержанием создаётся стакже, как список,
# только с круглыми скобками
a_tuple = (15, 'e', 500)
print(a_tuple)
# Или тоже самое, но с функцией tuple (предпочтительный вариант)
a_tuple = tuple((15, 'e', 500))
print(a_tuple)
# Доступ к эелементам кортежа
f_tuple = tuple(("Hello", ",", "World!"))
print(f_tuple[0])
#del f_tuple
#print(f_tuple)
# Преобразование кортажа в список и обратно
lst = [2.3, "a", 7, 1024] # Созжаём список
print(type(lst), lst)
tpl = tuple(lst); # Перобразовываем список в кортеж 
print(type(tpl), tpl)
# Обратная операция
tpl = (700, 8.93, "mix") # Создвём кортеж
print(type(tpl), tpl)
lst = list(tpl) # Преобразовыывем кортеж в список
print(type(lst), lst)
