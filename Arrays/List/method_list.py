# Сортировка содержимого списка
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Сортировать элементы списка в обратном порядке
a_list.reverse()
print(a_list)
# Сортировать элементы списка по возрастанию
a_list = [5, 1, 10, 3, 6, 2, 7, 8, 4, 9]
a_list.sort()
print(a_list)
# Построение списков
b_list = []
for i in range(10): # Указываем общее количество елементов
    b_list.append(i)
print(b_list)
# Тоже самое, но с пользовательским вводом
#a_list = [i for i in range(int(input("Enter you num:")))]
#print(a_list)
# Получение чётных чисел ихимеющегося списка
a_list = [5, 1, 10, 3, 6, 2, 7, 8, 4, 9]
even_list = list(filter(lambda x: x % 2 == 0, a_list))
print(even_list)
# Такое же решеное, но через списковое включение
a_list = [5, 1, 10, 3, 6, 2, 7, 8, 4, 9]
even_list = [x for x in a_list if x % 2 == 0]
print(even_list)
