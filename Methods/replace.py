# Метод replace заменяет все вхождения (значения индексов) одной строки на другую и возвращает полученное
s = 'Abracadabra';
t = s.replace('ra', 'e') # (old, new)
print(s);
print(t);
print(s.replace('a', 'A'));
print(s.replace('a', '', 2)); # Более выборочный replace
