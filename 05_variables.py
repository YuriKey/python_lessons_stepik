var_1 = 10  # глобальная переменная
var_2 = 20  # глобальная переменная


def sum():
    var_1 = 30  # локальная переменная
    var_2 = 40  # локальная переменная
    result = var_1 + var_2
    print(result)

def sub():
    var_1 = 100  # локальная переменная
    result = var_1 - var_2
    print(result)


print(var_1, var_2)
sum()
sub()
