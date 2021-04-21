# Пример функции c выводом комментария функции на экран
def double(num):
    """Function to double the value"""
    return 2*num

doubleNum = double(3);
print(doubleNum);
print(double.__doc__);
