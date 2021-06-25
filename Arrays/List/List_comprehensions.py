# Генератор
import sys
a = [ i for i in range(10)] # Списковое включение
print("a - ", type(a), "", sys.getsizeof(a), "byte", a)
for val in a:
    print(val, end = ' ')
b = (i for i in range(10)) # Генератор
print("b - ", type(b), "", sys.getsizeof(b), "byte", b)
for val in a:
    print(val, end = ' ')

