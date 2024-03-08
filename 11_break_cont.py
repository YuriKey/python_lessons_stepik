# list = [1, 4, 8, 16, 6, 44]
# for f in list:
#     if f == 6:
#         print("six!")
#         break
#     print(f)

# login = input("what is your name?")
# while True:
#     if login == "Rusik":
#         print("It`s correct")
#         passw = input("input your password")
#         if passw == "0000":
#             print("that`s correct!")
#         else:
#             print("Go away, cunteater!")
#             break
#     else:
#         print("invalid login")
#         break

list = [1, 4, 8, 16, 6, 44, 88]
for f in list:
    if f == 44:
        print("44 - cabrones!")
        break
    elif f == 16:
        print("sixteen!")
    elif f == 1:
        print("chosen one!")
        continue
    print(f)