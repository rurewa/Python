# Срезы
# Создаём новый срез
a_slice = [x for x in range(10)]
print(a_slice)
# Получаем копию среза
b_slice = a_slice[:]
print(b_slice)    
# Получить первые 5 элементов из среза
print(b_slice[0:5])
# Получить со 2 по 7 элементов среза
print(b_slice[2:7])
# Взять из списка элементы с шагом 2
print(b_slice[::2])
# Взять из среза элементы с 1 по 8  с шагом 2
print(b_slice[1:8:2])
# Конструирование срезов
#a_slice = []
s = slice(0, 5, 1) # Начальное значение, конечное и шаг
print(a_slice[s])
s = slice(0, 8, 2)
print(a_slice[s])

