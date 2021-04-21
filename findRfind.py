# Поиск в строках с помощью методов find/rfind 
s = 'Abracadabra';
# Поиск слева. Находит первый индекс
print(s.find('abr')); # Выводит номер найденного индекса
print(s.find('Abr'));
print(s.find('aaa')); # Выводит -1, т.к. искомая подстрока не найдена
# Поиск справа. Находит последний индекс искомой подстроки
print(s.rfind('abr'));
print(s.rfind('br'));
# Поиск в срезе
my_str = 'barbarian'
print(my_str.find('bar'));  # 0
print(my_str.find('bar', 1));  # 3
print(my_str.find('bar', 1, 2));  # -1 (значение, начало, конец) 0...10
# Example
txt = 'Hello, my frend';
x = txt.find('frend');
print(x);
print(txt.find('He'));
