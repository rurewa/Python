# Примеры работы со списками
a = [] # Объявление пустого списка
print(type(a)) # Метод type возвращает тип указанного объекта

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
a = [5, 0, 12, 9]
print(a) # Вывод всего содержимого списка

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
a = [5, 0, 12, 9]
print(a[0], a[3]) # Вывод только первого и последнего объекта списка

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# Можно создать копию списка
a = [5, 0, 12, 9]
b = a
print(b)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# Изменение содержимого списка
a = [5, 0, 12, 9]
a[1] = 11 # Изменение объекта в списке под индексом 1
print(a)

