# Литералы списка, кортежей, словарей, набора
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
multyNumbers = (23, 'program', 1+3j); # tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

# Списки (list)
print(type(fruits), fruits);
print(fruits[2]); # Доступ к элементу списка
print(fruits[0:2]); # Доступ к 2-м элементам списка
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Кортеж
print(type(numbers), numbers);
print(numbers[0]);
print(numbers[1:3]);
print(multyNumbers[1]);
print(multyNumbers[0:2]);
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Словарь
print(type(alphabets), alphabets);
print(alphabets['a']);

#-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print(type(vowels), vowels); # получить доступ к set пока не знаю!

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# int, float, str
print(10/5);
integerVar = int('123');
print("Integer var: ", integerVar);
a = 5;
print(a, " is of type ", type(a));
floatVar = float('123');
print("Float var: ", floatVar);
stringVar = str('123a');
b = 2.3;
print(b, " is of type ", type(b));
print("String var: ", stringVar);
firstWorld = str('Hello,');
secondWorld = str(' World!');
print(firstWorld + secondWorld);
c = int(1234567890123456789);
print(c);

