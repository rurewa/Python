# Простая программка, которая проверяет введённое число на соответствие 0-ю
num = float(input("Enter a number: "))
if num == 0:
    result = "The number was zero"
if num != 0:
    result = "The number was not zero"

print(result)     
