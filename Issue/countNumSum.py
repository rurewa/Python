# Задача определения количества цифр натуральногочисла n и их суммы
s = 0;
n = int(input()); #
count = 0;

while n > 0: #
    count += 1; #
    s += n % 10; #
    n //= 10; #
print(count); #
print(s); #    
