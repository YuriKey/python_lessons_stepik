# def description(name, age, sex):
#     print(f"Имя {name}, возраст - {age}, пол - {sex}.")
#
#
# description("Fiona", 28, "female")  # позиционный аргумент
# description(name=28, age="Fiona", sex="female")  # именованный аргумент

user_name = "Deby"
user_age = 16


def description(name, age, sex):
    print(f"Имя {name}, возраст - {age}, пол - {sex}.")


description(user_name, user_age, "female")
