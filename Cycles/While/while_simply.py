# Цикл итераций с помощью инкремента
i = 1
while i <= 5:
    print(i)
    i += 1

# Ещё пример цикла
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
a = 0 
while a < 7:
    print("A") # A будет выведена 7 раз в столбик
    a += 1

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# Пример бесконечного цикла
#while True:
#    print("infinity")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# Применение break
a = 0
while a >= 0:
    a += 1
    print(a)
    if a == 7:
        break     
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# Применение continue
a = -1
while a < 10:
    a += 1
    if a >= 7:
        continue
    print(a, "A")    
