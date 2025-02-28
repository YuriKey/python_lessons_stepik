# Пароль представляет из себя строку S из маленьких латинских букв длины N.
# Чтобы изменить пароль, Витя выбирает две позиции в строке — a и b — и меняет элементы на позициях a и b местами.
# написать программу, которая по заданным S, a, b будет генерировать новый пароль.

# Формат входных данных
# В первой строке задается пароль, который хочет поменять Витя, — S — строка длины N
# (1≤N≤200). Во второй строке через пробел записаны числа a и b (1≤a≤b≤N).
# Формат выходных данных
# Выведите единственную строку — новый пароль, полученный из S перестановкой символов.

def chars_replace():
    while True:
        s = input("enter password: ")
        n = len(s)

        if not s.isalpha():
            print("password contains an incorrect data")
            continue

        if n < 1 or n > 200:
            print("password have incorrect size")
            continue

        user_chars = input("enter chars numbers separated by a space: ").split()

        if len(user_chars) != 2:
            print("needs only a two chars")
            continue

        if not user_chars[0].isdigit() or not user_chars[1].isdigit():
            print("incorrect data type")
            continue

        a, b = int(user_chars[0]), int(user_chars[1])

        if a < 1 or a > n or b < 1 or b > n:
            print("some char number is incorrect")
            continue

        s = list(s)
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
        print( "".join(s))
        break


chars_replace()




