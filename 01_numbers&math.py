# определение типа данных переменной
num_1 = 5
print(num_1)
print(type(num_1))

# Сложение
num_2 = 3
num_3 = 8
result = num_2 + num_3
print(result)
result = -(num_2 + num_3)
print(result)

# Вычитание
num_4 = 80
num_5 = 16
result = num_4 - num_5
print(result)

# Умножение
num_6 = 35
num_7 = 5
result = num_6 * num_7
print(result)

# Возведение в степень
num_8 = 3
num_9 = 3
result = num_8 ** num_9
print(result)

# Деление
num_10 = 15
num_11 = 6
result = num_10 / num_11
print(result)

# остаток от деления
num_12 = 80
num_13 = 6
result = num_12 % num_13
print(result)

# сравнение
num_14 = 80
num_15 = 6
print(num_14 == num_15)
print(num_14 > num_15)
print(num_14 < num_15)
print(num_14 >= num_15)
print(num_14 <= num_15)
print(num_14 != num_14)

# округление
num_17 = 19
num_18 = 7
print(round(num_17 / num_18))
print(float(num_17 / num_18))

# округление до n после запятой
num_19 = 19
num_20 = 7
print(round(num_17 / num_18, 3))
print(float(num_17 / num_18))

# сведение к одному типу данных
num_21 = float(10.99)  # задаем переменную типа float
num_22 = 2  # задаем переменную типа int
result = int(num_21 + num_22)
print(result)
# или
result = num_21 + num_22
print(int(result))
