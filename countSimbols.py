# Подсёт заданных символов в строке
count = 0;
print("Enter world");
s = str(input());
for i in range(len(s)):
    if s[i] == 'a':
        count += 1;
    #if s[i] == 'a': count += 1; # Можно записать так    
print(count);
