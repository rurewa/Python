# Работа со словарями
# Создаём пустой словарь
dic = dict()
print(type(dic))
# Создаём словарь с заданными данными
dic = dict(Ivan = "manager", Mark = "worker")
print(dic)
# Создаём словарь с заданными данным по-другому
dic = {"Ivan" : "manager", "Mark" : "worker"}
print(dic)
# Добавляем элемент в словарь
dic = {"Russia" : "Moscow", "USA" : "New York"}
dic["China"] = "Pekin"
print(dic)
# Удаляем элемент из словаря
del dic["China"]
print(dic)
# Проверка ключа
print("Russia" in dic)
print("China" in dic)
# Доступ к элементу словаря
dic = {"Russia" : "Moscow", "USA" : "New York"}
print(dic["USA"])
# Удалить все элементы словаря
dic = {"Russia" : "Moscow", "USA" : "New York"}
dic.clear()
print(dic)
dic = {"Russia" : "Moscow", "USA" : "New York"}
# Копирование словаря
dic_copy = dic.copy()
print("dic_copy:", dic_copy)
# Создание нового словаря с ключом seq и значением value
my_new_dict = dict.fromkeys(['one', 'two', 3], 10)
print(my_new_dict)
# Возвращает значение словаря по ключу
dic = {"Russia" : "Moscow", "USA" : "New York"}
print(dic.get("Russia"))
# Возвращает содержимое словаря в форматированном виде
dic = {"Russia" : "Moscow", "USA" : "New York"}
print(dic.items())
# Возвращает только ключи словаря
dic = {"Russia" : "Moscow", "USA" : "New York"}
print(dic.keys())
# Удаление элемента по ключу
#dic = {"Russia" : "Moscow", "USA" : "New York"}
#print(dic.pop("USA"))
# Удаляет и возвращает пару ключ/значение из словаря. если словарь пуст, то будет вызвано исключение KeyError.
dic = {"Russia" : "Moscow", "USA" : "New York"}
print(dic.popitem())
print(dic)
