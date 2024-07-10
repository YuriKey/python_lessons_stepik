# age = 2
# name = "neo"
# if age == 25 and name == "neo":
#     print("I`m 25 years old and my name is Neo")
# elif age > 25:
#     print("I`m oldest than 25 years old.")
# else:
#     print("I`m youngest than 25 years old.")

# name = "Alex"
# if "a" in name:
#     print("My name is Alex")
# else:
#     print("My name is not Alex")

pin = 1234
print("Hello! Enter please your pin code: ")
user_pin = int(input())

if pin == user_pin:
    print("It`s okay. Take your money, asshole!")
else:
    print("Wrong, motherfucker!!! Go away! You have only 2 attempts.")
    print("Enter please your pin code: ")
    user_pin = int(input())
    if pin == user_pin:
        print("It`s okay. Take your money, bastard!")
    else:
        print("Wrong, motherfucker!!! Go away! You have only 1 attempts.")
        print("Enter please your pin code: ")
        user_pin = int(input())
        if pin == user_pin:
            print("It`s okay. Take your money, asshole!")
        else:
            print("Wrong, motherfucker!!! You have no one attempts. Go to the bank.")
            print("Hasta la vista, cabron!")
