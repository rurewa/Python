# примеры работы со списками в Python
# Простой вывод содержимого списка
a_list = [9, 0, 'x', 1]
print(type(a_list), a_list) # Вывод списка с указанием типа данных
# Доступ к индексам списка
print(a_list[1], a_list[3])
b_list = a_list # Ссылка (не копия) на список
print(b_list)
# Изменение объекта списка по индексу
b_list[2] = 3
b_list[3] = -1
b_list[0] = 'e'
print(b_list) # Вывод ссылки на a_list
print(a_list) # Вывод содержимого a_list
# Сделать копию списка
c_list = list(a_list)
print(type(c_list), c_list)
# Добавить элемент в конец списка
c_list.append("Hello")
print("Show c_list:", c_list[-1]) # Получить доступ к последнему элементу индекса
# Доступ к нескольким элементам списка в диапазоне индексов
print(c_list[0:2])
# Удаление элемента из списка по его значению
c_list.remove('e')
print("c_list remove:", c_list)
# Удаление элемента из списка по его индексу
del c_list[3]
print("c_list delete:", c_list)
# Очистить список
c_list = []
print("c_list clear:", c_list)
# Методы списка
c_list = [-5, 20, "Hello", 38, 60] # Объявляем список заново
print(c_list)
# Добавить новый элемент в конец списка
c_list[len(c_list):] = [25] # Эквивалентно c_list.append("25")
print(c_list)
# Добавление всех элементов из другого списка
e_list = [1, 2, -3]
c_list.extend(e_list)
print(c_list)
# Вставить элемент в нужную позицию
e_list.insert(0, 555) # 0 - индекс в списке. 555 - новый элемент
print(e_list)
# Удалить известный элемент из списка
e_list.remove(-3)
print(e_list)
# Удаляет элемент из позиции
e_list.pop(2) # 2 - номер индекса в списке
print(e_list)
# Удалить все элементы из списка
e_list.clear()
print("Clear list:", e_list)
# Возвратить индекс элемента
e_list = [58, -11, 25, 7.36, "Ok!"]
print(e_list)
print(e_list.index(-11))
# Вернуть количество указанных элементов в списке
e_list.append("Ok!") # Добавляем элемент
print(e_list)
print(e_list, " 'e' - ", e_list.count("Ok!"))
# Объединение списков с помощью оператора +
combo_list = e_list + a_list
print("Combo list:", combo_list)
