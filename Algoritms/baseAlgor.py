#
# Следование (линейный алгоритм)
x = 5
y = 6
print(x + y)
# Развилка
# Неполная развилка
x = 7
if x == 5:
    print(x)
# Полная развилка
x = 1
if x == 0:
    print("True")
else:
    print("False")
# Множественный выбор if/elif/else
x = 10
a = 3
if a < x:
    print(True)
elif a > x:
    print(False)
else:    
    print(False)
# Цикл for
#for i in range(10): # Вывести 10 раз слово Hello
#    print(i, "Hello")
# Цикл for с условием
#for i in range(10):
#    print(i, "Hello")
#    if i == 5:
#        break
# В цикле for можно применить полную развилку 
for i in range(10):
    if i == 5:
        continue
    else:    
        print(i, "Hello")
