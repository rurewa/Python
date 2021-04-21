# Работа с переменными в Python
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from collections import namedtuple # Подключаем коллекцию для создания констант в Python
Constants = namedtuple('Constants', ['pi', 'e']); # Определяем метод и переменные
constants = Constants(3.14, 2.718); # Инициализируем переменные
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=
number = 10.0;
links = "yandex.ru";

a, b, c = 5, 10.1, "Hello"; # Объявление и инициализация в одной строке

y = (1 == True);
w = True; # Можно и False

PI = 3.14;
PI = 6; # Жесть! Оказывается константы в Python легко перезаписать!

#constants.e = 3; # Перезапись константы теперь приведёт к ошибке. Ура!

# Типы литералов
x = 0b1111;
d = 0x12c;
string = "This is Python";
char = "C";
multiline_str = """Многострочный 
                                литерал""";
raw_str = r"raw \n string";

firstNum = 3;
secondNum = 2;
sumNum = firstNum * secondNum;

print(number);
print(links);
print(a);
print(b);
print(c);
print("PI: ", PI);
print("Константа: ", constants.pi); # Выводим значенеие консатнты
print("Binary literal: ", x, x.imag, x.real);
print("Hex literal: ", d);
print(string, " ", char);
print(type(multiline_str), multiline_str);
print(raw_str);
print(y);
print(w);
print(True & False);
print(True | False);
print("Sum: ", sumNum);

