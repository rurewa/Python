# Пример конвертирования типов
numInt = 103;
numStr = "103";

print("Data type of num_int: ", type(numInt));
print("Data type of num_str before Type Casting: ", type(numStr));

numStr = int(numStr); # Тут происходит конвертирование строки в число

print("Data type of num_str after Type Casting: ", type(numStr));

numSum = numInt + numStr;

print("Sum of num_int and num_str: ",  numSum);
print("Data type of the sum:", type(numSum));
