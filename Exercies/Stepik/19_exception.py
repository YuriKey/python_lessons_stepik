# a = int(input('Input first value: '))
# b = int(input('Input second value: '))
# result = int(a / b)
# print('Result is: ' + str(result))

# ZeroDivisionError
a = int(input('Input first value: '))
b = int(input('Input second value: '))
try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("You can`t substitute zero.")

print('Result is: ' + str(result))
